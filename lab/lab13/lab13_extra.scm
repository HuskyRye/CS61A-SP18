; Q4
(define (rle s)
;	(define (helper stream prev times)
;		(cond ((null? stream) (cons times nil))
;			  ((= (car stream) prev) (helper (cdr-stream stream) prev (+ 1 times)))
;			  (else (cons times stream))))
;	(if (null? s) nil	
;		(begin (define ret-value (helper (cdr-stream s) (car s) 1))
;		(cons-stream (list (car s) (car ret-value)) (rle (cdr ret-value)))))
	(define (helper stream prev times)
		(cond ((null? stream) (cons-stream (list prev times) nil))
			  ((= (car stream) prev) (helper (cdr-stream stream) prev (+ times 1)))
			  (else (cons-stream (list prev times) (helper (cdr-stream stream) (car stream) 1)))))
	(if (null? s) nil (helper (cdr-stream s) (car s) 1))
)

; Q4 testing functions
(define (list-to-stream lst)
    (if (null? lst) nil
                    (cons-stream (car lst) (list-to-stream (cdr lst))))
)

(define (stream-to-list s)
    (if (null? s) nil
                 (cons (car s) (stream-to-list (cdr-stream s))))
)

; Q5
(define (insert n s)
  'YOUR-CODE-HERE
)

; Q6
(define (deep-map fn s)
  'YOUR-CODE-HERE
  nil
)

; Q7
; Feel free to use these helper procedures in your solution
(define (map fn s)
  (if (null? s) nil
      (cons (fn (car s))
            (map fn (cdr s)))))

(define (filter fn s)
  (cond ((null? s) nil)
        ((fn (car s)) (cons (car s)
                            (filter fn (cdr s))))
        (else (filter fn (cdr s)))))

; Implementing and using these helper procedures is optional. You are allowed
; to delete them.
(define (unique s)
  'YOUR-CODE-HERE
  nil
)

(define (count name s)
  'YOUR-CODE-HERE
  nil
)

(define (tally names)
  'YOUR-CODE-HERE
  nil
)