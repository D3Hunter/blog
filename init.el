(setq require-final-newline t)
(global-linum-mode 1)
(setq make-backup-files nil)
(menu-bar-mode -1)
(tool-bar-mode -1)
(scroll-bar-mode -1)
(setq default-tab-width 4)
(setq-default c-basic-offset 4)
(setq column-number-mode t)
(setq-default indent-tabs-mode nil)

(require 'whitespace)
;; (setq whitespace-style '(face empty tabs lines-tail trailing))
(setq whitespace-style '(face empty tabs trailing))
(global-whitespace-mode t)

(setq c-default-style "linux" c-basic-offset 4)

;; (defun redraw-after-change (beg end len)
;;   (redraw-display))

;; (add-hook 'after-change-functions
;;            'redraw-after-change)

;; Move window in a fast way
;; (global-set-key [C-<right>] 'windmove-right)
;; (global-set-key [M-<up>] 'windmove-left)
;; (global-set-key (kbd "ESC-<up>") 'windmove-up)
;; (global-set-key (kbd "ESC-<down>") 'windmove-down)
;; (windmove-default-keybindings 'shift)
(global-set-key (kbd "C-x <left>")  'windmove-left)
(global-set-key (kbd "C-x <right>") 'windmove-right)
(global-set-key (kbd "C-x <up>")    'windmove-up)
(global-set-key (kbd "C-x <down>")  'windmove-down)
(global-set-key (kbd "C-2") 'set-mark-command)

(defun on-after-init ()
  (unless (display-graphic-p (selected-frame))
    (set-face-background 'default "unspecified-bg" (selected-frame))))

(add-hook 'window-setup-hook 'on-after-init)

(defun toggle-fullscreen ()
  "Toggle full screen on X11"
  (interactive)
  (when (eq window-system 'x)
    (set-frame-parameter
     nil 'fullscreen
     (when (not (frame-parameter nil 'fullscreen)) 'fullboth))))
(global-set-key [f11] 'toggle-fullscreen)

(setq inhibit-splash-screen t)
(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(ansi-color-faces-vector
   [default default default italic underline success warning error])
 '(ansi-color-names-vector
   ["#2d3743" "#ff4242" "#74af68" "#dbdb95" "#34cae2" "#008b8b" "#00ede1" "#e1e1e0"])
 '(custom-enabled-themes nil))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 )

;; (add-to-list 'load-path "~/.emacs.d/")
;; (require 'workgroups)
;; add-hook 'desktop-save-hook 'policy-switch-remove-unprintable-entities)
;; (require 'php-mode)
;; (load-file "~/.emacs.d/nhexl-mode-0.1.el")
