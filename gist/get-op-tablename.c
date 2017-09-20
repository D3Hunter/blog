char * util_sql_shift_to_keyword(char *sql)
{
    char *ret;
    char *p;
    size_t len;

    ret = NULL;

    if (!sql) {
        return ret;
    }

    for (p = sql; *sql; sql = p + 2)
    {
        len = strspn(sql, " \r\n\t\v\f");
        p = sql + len;
        if (p[0] != '/' || p[1] != '*')
            break;
        p += 2;

        while (*p)
        {
            if (p[0] == '*' && p[1] == '/')
                break;
            ++p;
        }

        if (*p) {
            log_debug("sql: unmatching '/*  */' in comment")
            goto finished;
        }
    }

    ret = sql;

finished:
    return ret;
}

typedef struct
{
    char *name;
    int len;
    int mode;// 1 update, 2 from, 3 into
}util_sql_operation;

#define UTIL_SQL_MODE_UPDATE 1
#define UTIL_SQL_MODE_FROM   2
#define UTIL_SQL_MODE_INTO   3
util_sql_operation util_sql_operations[] = {
    {"select",  6, UTIL_SQL_MODE_FROM},
    {"update",  6, UTIL_SQL_MODE_UPDATE},
    {"insert",  6, UTIL_SQL_MODE_INTO},
    {"replace", 7, UTIL_SQL_MODE_INTO},
    {"delete",  6, UTIL_SQL_MODE_FROM}
};

void util_sql_parse_sql(char *sql, char **op_name, char **tablename)
{
    int               mode;
    char              curr;
    size_t            len, lspec;
    util_sql_operation *op;

    if (!tablename || !op_name) {
        return;
    }

    *tablename = *op_name = NULL;

    p = util_sql_shift_to_keyword(sql);
    if (!p) {
        return;
    }

    for (op = util_sql_operations; op->name; op++) {
        if (strncasecmp(p, op->name, op->len) != 0) {
            continue;
        }
    }

    if (!op->name) {
        return;
    }

    mode = op->mode;
    *op_name = op->name;

    if (UTIL_SQL_MODE_UPDATE == mode) {
        p += strcspn(p, " \r\n\t\v\f");
        goto get_table_name;
    }

    while (*p) {
        p = util_sql_shift_to_keyword(p);
        if (!p) {
            break;
        }

        if (*p == '\'' || *p == '\"') {
            curr = *p;

            matching = strchr(p + 1, curr);
            if (!matching) {
                log_debug("sql: unmatching %c", curr);
                return;
            }

            p = matching + 1;

            continue;
        }

        if (UTIL_SQL_MODE_FROM == mode && 0 != strncasecmp(p, "from", 4)) {
            goto skip;
        } else if (0 != strncasecmp(p, "into", 4)) {
            goto skip;
        }

        /* match */
        if (strchr(" \r\n\t\v\f'\"`([@{", p[4])) {
            p += 4;

            break;
        }

    skip:
        p += strcspn(p, " \r\n\t\v\f'\"");
    }
    return;

get_table_name:
    p = util_sql_shift_to_keyword(p);
    if (!p) {
        return;
    }

    curr = *p;
    if (curr == '(') {
        ++p;

        curr = *p;
        if (curr != '`' && curr != '\'' && curr != '"') {
            len = strcspn(p, " \r\n\t\v\f,`)'\";");

            next = p[len];
            if (next != ',' && next != ')') {
                log_debug("sql: returning success: '(subquery)'");
                *tablename = strdup("(subquery)");
                return;
            }
        }
    }

    len = 0;
    while (1) {
        if (curr == '"' || curr == '\'' || curr == '`' || curr == '{') {
            ++p;
        }

        /* skip database */
        len = strcspn(p, " \r\n\t\v\f'\"`([@{]});,*./");
        lspec = strspn(p + len, " \r\n\t\v\f'\"`([@{]});,*/");
        if (*(p + len + lspec) != '.') {
            break;
        }

        p += len + lspec + 1;
        curr = *p;
    }

    if (len > 0) {
        *tablename = strndup(p, len);
        log_debug("sql: returning success: '%.100s'", *tablename);
    } else {
        log_debug("sql: got empty tablename");
    }
}