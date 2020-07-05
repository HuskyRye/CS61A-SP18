(define (replicate x n)
	(if (= n 0) nil
	(cons x (replicate x (- n 1)))))
	
(define-macro (repeat-n expr n)
  `(eval (cons 'begin (replicate ',expr ,n)))
)

;(repeat-n (print '(resistance is futile)) 4)

;(replicate '(print '(resistance is futile)) 4)

;((print (quote (resistance is futile)))
; (print (quote (resistance is futile)))
; (print (quote (resistance is futile)))
; (print (quote (resistance is futile))))

;(begin (print '(resistance is futile))
;		(print '(resistance is futile))
;		(print '(resistance is futile))
;		(print '(resistance is futile)))

(define-macro (or-macro expr1 expr2)
  `(let ((v1 ,expr1))
    (if v1 v1 
		,expr2)))
	
(define (helper expr remove)
    (cond ((null? expr) nil)
		  (remove (helper (cdr expr) #f))
		  (else (cons (car expr) (helper (cdr expr) #t)))))

(define-macro (prune-expr expr)
  `(eval (cons (car ',expr) (helper (cdr ',expr) #f)))
)

(define (has-even? s)
  (cond ((null? s) #f)
		((even? (car s)) #t)
		(else (has-even? (cdr-stream s)))))	
(define (f x) (* 3 x))
(define nums (cons-stream 1 (cons-stream (f 3) (cons-stream (f 5) nil))))

(define (range-stream start end)
  (if (= start end)
	  nil
	  (cons-stream start (range-stream (+ 1 start) end))))
	  
(define (slice s start end)
  (cond ((= end 0) nil)
		((= start 0) (cons (car s) (slice (cdr-stream s) start (- end 1))))
		(else (slice (cdr-stream s) (- start 1) (- end 1)))))
; if end == 0:
;    return nil
; elif start == 0:
;    return cons(car(s), slice(cdr-stream(s), start, end-1))
; else:
;    return slice(cdr-stream(s), start-1, end-1) 

(define (combine-with f xs ys)
  (if (or (null? xs) (null? ys))
  nil
  (cons-stream
	(f (car xs) (car ys))
	(combine-with f (cdr-stream xs) (cdr-stream ys)))))
	
(define (naturals start)
  (cons-stream start (naturals (+ start 1)))
)

(define evens (combine-with + (naturals 0) (naturals 0)))

(define factorials
  (cons-stream 1 (combine-with * (naturals 1) factorials)))

(define fibs 
  (cons-stream 0 (cons-stream 1 (combine-with + fibs (cdr-stream fibs)))))

(define (x-stream n)
  (cons-stream n (x-stream n)))
  
(define (exp x)
  (cons-stream 1 
  (combine-with + (combine-with / (combine-with expt (x-stream x) 
													 (naturals 1))
								  (cdr-stream factorials))
				  (exp x))))