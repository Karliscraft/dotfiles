(set-module-dir "/home/void/stumpwm-contrib/")
(setf *startup-message* "StumpWM started correctly.")
(load-module "swm-gaps")
(load-module "ttf-fonts")
(xft:cache-fonts)
(set-font (make-instance 'xft:font :family "DejaVu Sans Mono" :subfamily "Book" :size 11))
(setf swm-gaps:*inner-gaps-size* 7)
(swm-gaps:toggle-gaps)
(setf *ignore-wm-inc-hints* t)
(setf *window-border-style* :none)
(defun update-title (to-frame from-frame)
  (run-shell-command "xfce4-panel --plugin-event=genmon-4:refresh:bool:true"))
(add-hook *focus-window-hook* 'update-title)



