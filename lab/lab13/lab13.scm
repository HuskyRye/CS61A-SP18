; Q1
;(define (compose-all funcs)
;  (cond ((null? funcs) (lambda (x) x))
;		((null? (cdr funcs)) (car funcs))
;		(else (compose-all (cons (compose (car funcs) (car (cdr funcs)))
;								 (cdr (cdr funcs)))))))
;(define (compose f g)
;	(define (h x)
;		(g (f x)))
;	h)

(define (compose-all funcs)
	(if (null? funcs)
		(lambda (x) x)
		(lambda (x) ((compose-all (cdr funcs))
					 ((car funcs) x)))))

; Q2
(define (tail-replicate x n)
	(define (helper x n lst)
		(if (= n 0) lst
			(helper x (- n 1) (cons x lst))))
	(helper x n nil)
)