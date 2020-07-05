(define (factorial x)
; if x == 1:
;   return 1
; else:
;   return x * factorial(x-1)
  (if (= x 1) 1
    (* x (factorial (- x 1))))
)

(define (fib n)
  (if (or (= n 0) (= n 1))
    n
	(+ (fib (- n 1)) (fib (- n 2))))
)

(define (concat a b)
; if a.rest == Link.empty:
;   return Link(a.first, b)
; else:
;   return Link(a.first, concat(a.rest b))
  (if (null? (cdr a))
    (cons (car a) b)
	(cons (car a) (concat (cdr a) b)))
)

(define (replicate x n)
  (if (= n 1)
  (cons x nil)
  (cons x (replicate x (- n 1))))
)

(define (uncompress s)
; if s == Link.empty:
;   return s
; else:
;   return(concat(replicate(s.first.first, s.first.rest.first), uncompress(s.rest)))
  (if (null? s)
    s
	(concat (replicate (car (car s)) (car (cdr (car s)))) (uncompress (cdr s))))
)

(define (map fn lst)
; if s == Link.empty:
;   return s
; else:
;   return Link(fn(lst.first), map(fn, lst.rest))
  (if (null? lst)
    lst
	(cons (fn (car lst)) (map fn (cdr lst))))
)

(define (deep-map fn lst)
; if lst == Link.empty:
;   return lst
; elif lst.first is Link:
;   return Link(deep-map(fn, lst.first), deep-map(fn, lst.second))
; else:
;   return Link(fn(lst.first), deep-map(fn, lst.second))
  (cond
    ((null? lst) lst)
	((list? (car lst)) (cons (deep-map fn (car lst)) (deep-map fn (cdr lst))))
	(else (cons (fn (car lst)) (deep-map fn (cdr lst)))))
)

(define (make-tree label branches)
  (cons label branches))
  
(define (label tree)
  (car tree))
  
(define (branches tree)
  (cdr tree))
  
(define (tree-sum tree)
; result = tree.label
; for branch in branches:
;   result += tree-sum(branch)
; return result
;
; return tree.label + sum(map(tree-sum, tree.branches))
  (define (sum lst)
	; if lst == Link.empty:
	;   return 0
	; else:
	;   return lst.first + sum(lst.rest)
	(if (null? lst)
		0
		(+ (car lst) (sum (cdr lst)))))
  (+ (label tree) (sum (map tree-sum (branches tree))))
)

; t = tree(1, [tree(2, [tree(5)]), tree(3), tree(4)])
(define t (make-tree 1 
				(list (make-tree 2 
							(list (make-tree 5 nil))) 
					  (make-tree 3 nil) 
					  (make-tree 4 nil))))
; (tree-sum t)