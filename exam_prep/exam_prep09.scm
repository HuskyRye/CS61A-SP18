(define (non-contiguous subseq lst)
	(cond ((null? subseq) True)
		  ((null? lst) False)
		  ((= (car subseq) (car lst)) 
				(non-contiguous (cdr subseq) (cdr lst)))
		  (else (non-contiguous subseq (cdr lst)))))
		  
(define (assert-equals expected expression)
	(if (eq? (eval expression) expected)
		'OK
		`(expected ,expected but got ,(eval expression))))
		
(define (directions n sym)
	(define (search s exp)
		(cond ((number? s) (if (= n s) exp nil))
			  ((null? s) nil)
			  (else (search-list s exp))))
	(define (search-list s exp)
		(let ((first (search (car s) `(car ,exp)))
			  (rest (search (cdr s) `(cdr ,exp))))
			  (if (null? first) rest first)))
	(search (eval sym) sym))
	
(define a '(1 (2 3) ((4))))
(define b '((3 4) 5))

;(if (= days-left 0) 
;	(begin (print 'im-free) 'jk-final))
	
(define (slice s start end)
  (cond ((= end 0) nil)
		((= start 0) (cons (car s) (slice (cdr-stream s) start (- end 1))))
		(else (slice (cdr-stream s) (- start 1) (- end 1)))))