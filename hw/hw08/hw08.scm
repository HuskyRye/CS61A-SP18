(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cdr (cdr s)))
)

(define (sign x)
  (cond ((> x 0) 1)
		((= x 0) 0)
		(else -1))
)

(define (square x) (* x x))

(define (pow b n)
  (cond ((= n 0) 1)
		((even? n) (square (pow b (/ n 2))))
		(else (* b (square (pow b (/ (- n 1) 2))))))
)

(define (ordered? s)
; if s == Link.empty:
;   return True
; elif s.first > s.rest.first:
;   return False
; else:
;   return ordered?(s.rest)
  (cond ((null? (cdr s)) True)
		((> (car s) (car (cdr s))) False)
		(else (ordered? (cdr s))))
)

(define (nodots s)
; if s == Link.empty:
;    return s
; elif s is int:
;    return Link(s, Link.empty)
; elif s.first is Link:
;    return Link(nodots(s.first), nodots(s.rest))
; else:
;    return Link(s.first, nodots(s.rest))
  (cond ((null? s) s)
		((number? s) (cons s nil))
		((pair? (car s)) (cons (nodots (car s)) (nodots (cdr s))))
		(else (cons (car s) (nodots (cdr s)))))
)

; Sets as sorted lists

(define (empty? s) (null? s))

(define (contains? s v)
    (cond ((empty? s) #f)
          ((> (car s) v) #f)
		  ((= (car s) v) #t)
		  (else (contains? (cdr s) v))
          ))

; Equivalent Python code, for your reference:
;
; def empty(s):
;     return s is Link.empty
;
; def contains(s, v):
;     if empty(s):
;         return False
;     elif s.first > v:
;         return False
;     elif s.first == v:
;         return True
;     else:
;         return contains(s.rest, v)

(define (add s v)
;  if s == Link.empty:
;    return Link(v)
;  elif s.first > v:
;    return Link(v, s)
;  elif s.first == v:
;    return s
;  else:
;    return Link(s.first, add(s.rest, v))
    (cond ((empty? s) (list v))
          ((> (car s) v) (cons v s))
		  ((= (car s) v) s)
		  (else (cons (car s) (add (cdr s) v)))
		  ))

(define (intersect s t)
    (cond ((or (empty? s) (empty? t)) nil)
		  ((= (car s) (car t)) (cons (car s) (intersect (cdr s) (cdr t))))
		  ((< (car s) (car t)) (intersect (cdr s) t))
		  (else (intersect s (cdr t)))
	))

; Equivalent Python code, for your reference:
;
; def intersect(set1, set2):
;     if empty(set1) or empty(set2):
;         return Link.empty
;     else:
;         e1, e2 = set1.first, set2.first
;         if e1 == e2:
;             return Link(e1, intersect(set1.rest, set2.rest))
;         elif e1 < e2:
;             return intersect(set1.rest, set2)
;         elif e2 < e1:
;             return intersect(set1, set2.rest)

(define (union s t)
; if s == Link.empty:
;   return t
; elif t == Link.empty:
;   return s
; elif s.first = t.first:
;   return Link(s.first, union(s.rest, t.rest))
; elif s.first < t.first:
;   return Link(s.first, union(s.rest, t))
; else:
;   return Link(t.first, union(s, t.rest))
    (cond ((empty? s) t)
          ((empty? t) s)
          ((= (car s) (car t)) (cons (car s) (union (cdr s) (cdr t))))
		  ((< (car s) (car t)) (cons (car s) (union (cdr s) t)))
		  (else (cons (car t) (union s (cdr t))))
          ))