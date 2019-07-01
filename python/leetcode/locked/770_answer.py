"""
Solution 1:
def basicCalculatorIV(self, expression, evalvars, evalints):
    class C(collections.Counter):
        def __add__(self, other):
            self.update(other)
            return self
        def __sub__(self, other):
            self.subtract(other)
            return self
        def __mul__(self, other):
            product = C()
            for x in self:
                for y in other:
                    xy = tuple(sorted(x + y))
                    product[xy] += self[x] * other[y]
            return product
    vals = dict(zip(evalvars, evalints))
    def f(s):
        s = str(vals.get(s, s))
        return C({(s,): 1}) if s.isalpha() else C({(): int(s)})
    c = eval(re.sub('(\w+)', r'f("\1")', expression))
    return ['*'.join((str(c[x]),) + x)
            for x in sorted(c, key=lambda x: (-len(x), x))
            if c[x]]
I let eval and collections.Counter do most of the work. First I wrap every variable and number in the given expression in a call to f. For example the expression e + 8 - a + 5 becomes f("e") + f("8") - f("a") + f("5"). Then when I eval that, my function f converts its argument to a C object, which is a subclass of Counter.

A term like 42*a*a*b is represented by C({('a', 'a', 'b'): 42}). That is, the key is the variables as sorted tuple, and the value is the coefficient. So f converts free variables to C({('x',): 1}) (where x is the variable name) and converts known variables or numbers to C({(): x}) (where x is the number).

Counters already know how to add and subtract each other, but I had to teach them multiplication. And in the end I need to turn the resulting C object into the desired output format.
"""

"""
Solution 2:
use stack to implement the arithmetic operation
We can give each operator a priority number, + and - is 0, while * is 1.
When an operator is inside "()", its priority increases by 2 for every "()".

For example:

4*(a-(b+(x*y))+d*e)
the operator priorities are:

* - + * + *
1 2 4 7 2 3
always do the operation with highest priority first.

class Term is for each single term in our final answer.
class Expression is a list of class Terms.
We can do +-* for two Expressions.

class Solution {
    Map<String,Integer> map=new HashMap<>(); //evaluation map
    class Term
    {
        int para=1; //the parameter of this term
        List<String> var=new ArrayList<>(); //each factor (e.a. a*b*b*c->{a,b,b,c})
        @Override
        public String toString()
        {
            if (para==0) return "";
            String ans="";
            for (String s:var) ans+="*"+s;
            return para+ans;
        }
        boolean equals(Term that)
        {
            if (this.var.size()!=that.var.size()) return false;
            for (int i=0;i<this.var.size();i++)
                if (!this.var.get(i).equals(that.var.get(i))) return false;
            return true;
        }
        int compareTo(Term that)
        {
            if (this.var.size()>that.var.size()) return -1;
            if (this.var.size()<that.var.size()) return 1;
            for (int i=0;i<this.var.size();i++)
            {
                int x=this.var.get(i).compareTo(that.var.get(i));
                if (x!=0) return x;
            }
            return 0;
        }
        Term times(Term that)
        {
            Term pro=new Term(this.para*that.para);
            for (String s:this.var) pro.var.add(new String(s));
            for (String s:that.var) pro.var.add(new String(s));
            Collections.sort(pro.var);
            return pro;
        }
        Term(int x) { para=x; }
        Term(String s) { if (map.containsKey(s)) para=map.get(s); else var.add(s); }
        Term(Term that) { this.para=that.para; this.var=new ArrayList<>(that.var); }
    }
    class Expression 
    {
        List<Term> list=new ArrayList<>(); //Term List
        char oper='+'; // Arithmetic symbol
        Expression(int x) { list.add(new Term(x)); }
        Expression(String s) { list.add(new Term(s)); }
        Expression(List<Term> l) { list=l; }
        Expression times(Expression that)
        {
            List<Term> c=new ArrayList<>();
            for (Term t1:this.list)
                for (Term t2:that.list)
                    c.add(t1.times(t2));
            c=combine(c);
            return new Expression(c);
        }
        Expression plus(Expression that,int sgn)
        {
            List<Term> c=new ArrayList<>();
            for (Term t:this.list) c.add(new Term(t));
            for (Term t:that.list) 
            {
                Term t2=new Term(t);
                t2.para=t2.para*sgn;
                c.add(t2);
            }
            c=combine(c);
            return new Expression(c);
        }
        Expression cal(Expression that)
        {
            if (oper=='+') return plus(that,1);
            if (oper=='-') return plus(that,-1);
            return times(that);
        }
        List<String> toList()
        {
            List<String> ans=new ArrayList<>();
            for (Term t:list) 
            {
                String s=t.toString();
                if (s.length()>0) ans.add(s);
            }
            return ans;
        }
    }  
    List<Term> combine(List<Term> a) //combine the similar terms
    {
        Collections.sort(a,(t1,t2)->(t1.compareTo(t2))); //sort all terms to make similar terms together
        List<Term> c=new ArrayList<>();
        for (Term t:a)
        {
            if (c.size()!=0 && t.equals(c.get(c.size()-1))) c.get(c.size()-1).para+=t.para;
            else c.add(new Term(t));
        }
        return c;
    }
    public List<String> basicCalculatorIV(String expression, String[] evalvars, int[] evalints) {
        for (int i=0;i<evalvars.length;i++) map.put(evalvars[i],evalints[i]);
        int i=0,l=expression.length();
        Stack<Expression> stack=new Stack<>();
        Stack<Integer> priStack=new Stack<>();
        Expression zero=new Expression(0);
        stack.push(zero);
        priStack.push(0);
        int pri=0;
        while (i<l)
        {
            char ch=expression.charAt(i);
            if (Character.isDigit(ch))
            {
                int num=0;
                while (i<l && Character.isDigit(expression.charAt(i)))
                {
                    num=num*10+(expression.charAt(i)-48);
                    i++;
                }
                stack.add(new Expression(num));
                continue;
            }
            if (Character.isLetter(ch))
            {
                String s="";
                while (i<l && Character.isLetter(expression.charAt(i)))
                {
                    s+=expression.charAt(i);
                    i++;
                }
                stack.add(new Expression(s));
                continue;
            }
            if (ch=='(') pri+=2;
            if (ch==')') pri-=2;
            if (ch=='+' || ch=='-' || ch=='*')
            {
                int nowPri=pri;
                if (ch=='*') nowPri++;
                while (!priStack.isEmpty() && nowPri<=priStack.peek())
                {
                    Expression now=stack.pop(),last=stack.pop();
                    priStack.pop();
                    stack.push(last.cal(now));
                }
                stack.peek().oper=ch;
                priStack.push(nowPri);
            }
            i++;
        }
        while (stack.size()>1)
        {
            Expression now=stack.pop(),last=stack.pop();
            stack.push(last.cal(now));
        }
        return stack.peek().toList();
    }
}
"""