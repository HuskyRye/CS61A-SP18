(define (fib n)
  (define (fib-sofar n prev curr)
    (if (= n 0)
		curr
		(fib-sofar (- n 1) curr (+ prev curr))))
  (fib-sofar n 1 0))
  
(define (sum lst)
  (define (sum-sofar lst result)
    (if (null? lst)
		result
		(sum-sofar (cdr lst) (+ result (car lst)))))
  (sum-sofar lst 0))

(define (reverse lst)
  (define (reverse-sofar lst lst-sofar)
    (if (null? lst) lst-sofar
	(reverse-sofar (cdr lst) (cons (car lst) lst-sofar))))
  (reverse-sofar lst nil))

(define (append a b)
  (define (rev-append-tail a b)
    (if (null? a) b
	(rev-append-tail (cdr a) (cons (car a) b))))
  (rev-append-tail (reverse a) b))
  
(define (insert n lst)
  (define (rev-insert lst rev-lst)
    (cond ((null? lst) (reverse (cons n rev-lst)))
		  ((> (car lst) n)(append (reverse rev-lst) (cons n lst)))
		  (else (rev-insert (cdr lst) (cons (car lst) rev-lst)))))
  (rev-insert lst nil))