;; Extra Scheme Questions ;;


(define lst
  ;; '((1) 2 (3 4) 5) 
  (list (list 1) 2 (list 3 4) 5)
)

(define (composed f g)
  ;; h(x) = f(g(x))
  (define (h x)
	(f (g x))
  )
  h
)

(define (filter f lst)
  (cond
	((null? lst) lst)
	((f (car lst)) (cons (car lst) (filter f (cdr lst))))
	(else (filter f (cdr lst))))
)

(define (remove item lst)
  (define (not-equal elem)
	(not (= elem item))
  )
  (filter not-equal lst)
)


;;; Tests
(remove 3 nil)
; expect ()
(remove 3 '(1 3 5))
; expect (1 5)
(remove 5 '(5 3 5 5 1 4 5 4))
; expect (3 1 4 4)

(define (no-repeats s)
  (if (null? s)
    nil
	(cons (car s) (no-repeats (remove (car s) (cdr s)))))
;  if s == Link.empty:
;	return Link.empty
;  else:
;	Link(s.first, no-repeats(remove(s.first, s.rest)))
)

(define (substitute s old new)
;  if s == Link.empty:
;	return s
;  elif s.first is pairs:
;   return Link(substitute(s.first, old, new), substitute(s.rest, old, new))
;  elif s.first == old:
;	return Link(new, substitute(s.rest, old, new))
;  else:
;	return Link(s.first, substitute(s.rest, old, new))
  (cond
    ((null? s) s)
	((pair? (car s)) (cons (substitute (car s) old new) (substitute (cdr s) old new)))
	((equal? (car s) old) (cons new (substitute (cdr s) old new)))
	(else (cons (car s) (substitute (cdr s) old new)))
  )
)

(define (sub-all s olds news)
;  if olds == Link.empty
;    return s
;  else:
;    return sub-all(substitue(s, olds.first, olds.second), olds.rest, news.rest)
  (if (null? olds) s
  (sub-all (substitute s (car olds) (car news)) (cdr olds) (cdr news)))
)