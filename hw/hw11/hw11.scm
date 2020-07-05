(define (find s predicate)
  (cond ((null? s) #f)
		((predicate (car s)) (car s))
		(else (find (cdr-stream s) predicate)))
)

(define (scale-stream s k)
  (cons-stream (* k (car s)) (scale-stream (cdr-stream s) k))
)

(define (in x s)
	(cond ((null? s) #f)
		  ((eq? (car s) x) #t)
		  (else (in x (cdr-stream s)))))

(define (has-cycle s)
;  if s is nil:
;	return false
;  elif s in has-seen
;	return true
;  else:
;    return helper(cdr-stream s, cons-stream(s, has-seen)
  (define (helper s has-seen)
	(cond ((null? s) #f)
		  ((in s has-seen ) #t)
		  (else (helper (cdr-stream s) (cons-stream s has-seen)))))
  (helper s nil)
)

(define (has-cycle-constant s)
  (define (helper a b)
    (cond ((or (null? a) (null? b) (null? (cdr-stream b))) #f)
		  ((eq? a b) #t)
		  (else (helper (cdr-stream a) (cdr-stream (cdr-stream b))))))
  (helper s (cdr-stream s))
)
