tell application "iTerm2"
    tell current window
        set load_tab to (create tab with default profile)
        tell current session of load_tab
            set vert_session to (split vertically with default profile)
            set left_buttom_session to (split horizontally with default profile)
            write text "ls"
        end tell
        tell left_buttom_session
            write text "ls"
        end tell

        tell vert_session
            set right_buttom_sesson to (split horizontally with default profile)
            write text "ls"
        end tell
        tell right_buttom_sesson
            write text "ls"
            select
        end tell
    end tell
end tell

