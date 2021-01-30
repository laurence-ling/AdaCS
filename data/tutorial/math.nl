1	UnivariateSolver , UnivariateDifferentiableSolver and PolynomialSolver provide means to find roots of univariate real-valued functions, differentiable univariate real-valued functions, and polynomial functions respectively.
2	A root is the value where the function takes the value 0.
3	Commons-Math includes implementations of the several root-finding algorithms:
4	In order to use the root-finding features, first a solver object must be created by calling its constructor, often providing relative and absolute accuracy.
5	Using a solver object, roots of functions are easily found using the BracketingNthOrderBrentSolver.solve methods.
6	These methods takes a maximum iteration count maxEval, a function f, and either two domain values, min and max, or a startValue as parameters.
7	If the maximal number of iterations count is exceeded, non-convergence is assumed and a ConvergenceException exception is thrown.
8	A suggested value is 100, which should be plenty, given that a bisection algorithm can't get any more accurate after 52 iterations because of the number of mantissa bits in a double precision floating point number.
9	If a number of ill-conditioned problems is to be solved, this number can be decreased in order to avoid wasting time.
10	Bracketed solvers also take an allowed solution enum parameter to specify which side of the final convergence interval should be selected as the root.
11	It can be ANY_SIDE, LEFT_SIDE, RIGHT_SIDE, BELOW_SIDE or ABOVE_SIDE.
12	Left and right are used to specify the root along the function parameter axis while below and above refer to the function value axis.
13	The solve methods compute a value c such that:
14	Typical usage:
15	Force bracketing, by refining a base solution found by a non-bracketing solver:
16	The BrentSolver uses the Brent-Dekker algorithm which is fast and robust.
17	If there are multiple roots in the interval, or there is a large domain of indeterminacy, the algorithm will converge to a random root in the interval without indication that there are problems.
18	Interestingly, the examined text book implementations all disagree in details of the convergence criteria.
19	Also each implementation had problems for one of the test cases, so the expressions had to be fudged further.
20	Don't expect to get exactly the same root values as for other implementations of this algorithm.
21	The BracketingNthOrderBrentSolver uses an extension of the Brent-Dekker algorithm which uses inverse nth order polynomial interpolation instead of inverse quadratic interpolation, and which allows selection of the side of the convergence interval for result bracketing.
22	This is now the recommended algorithm for most users since it has the largest order, doesn't require derivatives, has guaranteed convergence and allows result bracket selection.
23	The SecantSolver uses a straightforward secant algorithm which does not bracket the search and therefore does not guarantee convergence.
24	It may be faster than Brent on some well-behaved functions.
25	The RegulaFalsiSolver is variation of secant preserving bracketing, but then it may be slow, as one end point of the search interval will become fixed after and only the other end point will converge to the root, hence resulting in a search interval size that does not decrease to zero.
26	The IllinoisSolver and PegasusSolver are well-known variations of regula falsi that fix the problem of stuck end points by slightly weighting one endpoint to balance the interval at next iteration.
27	Pegasus is often faster than Illinois.
28	Pegasus may be the algorithm of choice for selecting a specific side of the convergence interval.
29	The BisectionSolver is included for completeness and for establishing a fall back in cases of emergency.
30	The algorithm is simple, most likely bug free and guaranteed to converge even in very adverse circumstances which might cause other algorithms to malfunction.
31	The drawback is of course that it is also guaranteed to be slow.
32	The UnivariateSolver interface exposes many properties to control the convergence of a solver.
33	The accuracy properties are set at solver instance creation and cannot be changed afterwards, there are only getters to retriveve their values, no setters are available.
34	A UnivariateInterpolator is used to find a univariate real-valued function f which for a given set of ordered pairs (xi,yi) yields f(xi)=yi to the best accuracy possible.
35	The result is provided as an object implementing the UnivariateFunction interface.
36	It can therefore be evaluated at any point, including point not belonging to the original set.
37	Currently, only an interpolator for generating natural cubic splines and a polynomial interpolator are available.
38	There is no interpolator factory, mainly because the interpolation algorithm is more determined by the kind of the interpolated function rather than the set of points to interpolate.
39	There aren't currently any accuracy controls either, as interpolation accuracy is in general determined by the algorithm.
40	Typical usage:
41	A natural cubic spline is a function consisting of a polynomial of third degree for each subinterval determined by the x-coordinates of the interpolated points.
42	A function interpolating N value pairs consists of N-1 polynomials.
43	The function is continuous, smooth and can be differentiated twice.
44	The second derivative is continuous but not smooth.
45	The x values passed to the interpolator must be ordered in ascending order.
46	It is not valid to evaluate the function for values outside the range x0.
47	.
48	xN.
49	Microsphere interpolation is a robust multidimensional interpolation algorithm.
50	It has been described in William Dudziak's MS thesis.
51	Hermite interpolation is an interpolation method that can use derivatives in addition to function values at sample points.
52	The HermiteInterpolator class implements this method for vector-valued functions.
53	The sampling points can have any spacing (there are no requirements for a regular grid) and some points may provide derivatives while others don't provide them (or provide derivatives to a smaller order).
54	Points are added one at a time, as shown in the following example:
55	A BivariateGridInterpolator is used to find a bivariate real-valued function f which for a given set of tuples (xi,yj,fij) yields f(xi,yj)=fij to the best accuracy possible.
56	The result is provided as an object implementing the BivariateFunction interface.
57	It can therefore be evaluated at any point, including a point not belonging to the original set.
58	The arrays xi and yj must be sorted in increasing order in order to define a two-dimensional grid.
59	In bicubic interpolation, the interpolation function is a 3rd-degree polynomial of two variables.
60	The coefficients are computed from the function values sampled on a grid, as well as the values of the partial derivatives of the function at those grid points.
61	From two-dimensional data sampled on a grid, the BicubicSplineInterpolator computes a bicubic interpolating function.
62	Prior to computing an interpolating function, the SmoothingPolynomialBicubicSplineInterpolator class performs smoothing of the data by computing the polynomial that best fits each of the one-dimensional curves along each of the coordinate axes.
63	A TrivariateGridInterpolator is used to find a trivariate real-valued function f which for a given set of tuples (xi,yj,zk, fijk) yields f(xi,yj,zk)=fijk to the best accuracy possible.
64	The result is provided as an object implementing the TrivariateFunction interface.
65	It can therefore be evaluated at any point, including a point not belonging to the original set.
66	The arrays xi, yj and zk must be sorted in increasing order in order to define a three-dimensional grid.
67	In tricubic interpolation, the interpolation function is a 3rd-degree polynomial of three variables.
68	The coefficients are computed from the function values sampled on a grid, as well as the values of the partial derivatives of the function at those grid points.
69	From three-dimensional data sampled on a grid, the TricubicSplineInterpolator computes a tricubic interpolating function.
70	A UnivariateIntegrator provides the means to numerically integrate univariate real-valued functions.
71	Commons-Math includes implementations of the following integration algorithms:
72	The org.apache.commons.math3.analysis.polynomials package provides real coefficients polynomials.
73	The PolynomialFunction class is the most general one, using traditional coefficients arrays.
74	The PolynomialsUtils utility class provides static factory methods to build Chebyshev, Hermite, Jacobi, Laguerre and Legendre polynomials.
75	Coefficients are computed using exact fractions so these factory methods can build polynomials up to any degree.
76	The org.apache.commons.math3.analysis.differentiation package provides a general-purpose differentiation framework.
77	The core class is DerivativeStructure which holds the value and the differentials of a function.
78	This class handles some arbitrary number of free parameters and arbitrary derivation order.
79	It is used both as the input and the output type for the UnivariateDifferentiableFunction interface.
80	Any differentiable function should implement this interface.
81	The main idea behind the DerivativeStructure class is that it can be used almost as a number (i.e. it can be added, multiplied, its square root can be extracted or its cosine computed... However, in addition to computed the value itself when doing these computations, the partial derivatives are also computed alongside.
82	This is an extension of what is sometimes called Rall's numbers.
83	This extension is described in Dan Kalman's paper Doubly Recursive Multivariate Automatic Differentiation, Mathematics Magazine, vol. 75, no. 3, June 2002.
84	Rall's numbers only hold the first derivative with respect to one free parameter whereas Dan Kalman's derivative structures hold all partial derivatives up to any specified order, with respect to any number of free parameters.
85	Rall's numbers therefore can be seen as derivative structures for order one derivative and one free parameter, and primitive real numbers can be seen as derivative structures with zero order derivative and no free parameters.
86	The workflow of computation of a derivatives of an expression y=f(x) is the following one.
87	First we configure an input parameter x of type DerivativeStructure so it will drive the function to compute all derivatives up to order 3 for example.
88	Then we compute y=f(x) normally by passing this parameter to the f function.At the end, we extract from y the value and the derivatives we want.
89	As we have specified 3rd order when we built x, we can retrieve the derivatives up to 3rd order from y.
90	The following example shows that (the 0 parameter in the DerivativeStructure constructor will be explained in the next paragraph):
91	When we compute y from this setting, what we really do is chain f after the identity function, so the net result is that the derivatives are computed with respect to the indexed free parameters (i.e. only free parameter number 0 here since there is only one free parameter) of the identity function x. Going one step further, if we compute z = g(y), we will also compute z as a function of the initial free parameter.
92	The very important consequence is that if we call z.DerivativeStructure.getPartialDerivative(1) , we will not get the first derivative of g with respect to y, but with respect to the free parameter p0: the derivatives of g and f will be chained together automatically, without user intervention.
93	This design choice is a very classical one in many algorithmic differentiation frameworks, either based on operator overloading (like the one we implemented here) or based on code generation.
94	It implies the user has to bootstrap the system by providing initial derivatives, and this is essentially done by setting up identity function, i.e. functions that represent the variables themselves and have only unit first derivative.
95	This design also allow a very interesting feature which can be explained with the following example.
96	Suppose we have a two arguments function f and a one argument function g.
97	If we compute g(f(x, y)) with x and y be two variables, we want to be able to compute the partial derivatives dg/dx, dg/dy, d2g/dx2 d2g/dxdy d2g/dy2.
98	This does make sense since we combined the two functions, and it does make sense despite g is a one argument function only.
99	In order to do this, we simply set up x as an identity function of an implicit free parameter p0 and y as an identity function of a different implicit free parameter p1 and compute everything directly.
100	In order to be able to combine everything, however, both x and y must be built with the appropriate dimensions, so they will both be declared to handle two free parameters, but x will depend only on parameter 0 while y will depend on parameter 1.
101	Here is how we do this (note that DerivativeStructure.getPartialDerivative is a variable arguments method which take as arguments the derivation order with respect to all free parameters, i.e. the first argument is derivation order with respect to free parameter 0 and the second argument is derivation order with respect to free parameter 1):
102	There are several ways a user can create an implementation of the UnivariateDifferentiableFunction interface.
103	The first method is to simply write it directly using the appropriate methods from DerivativeStructure to compute addition, subtraction, sine, cosine... This is often quite straigthforward and there is no need to remember the rules for differentiation: the user code only represent the function itself, the differentials will be computed automatically under the hood.
104	The second method is to write a classical UnivariateFunction and to pass it to an existing implementation of the UnivariateFunctionDifferentiator interface to retrieve a differentiated version of the same function.
105	The first method is more suited to small functions for which user already control all the underlying code.
106	The second method is more suited to either large functions that would be cumbersome to write using the DerivativeStructure API, or functions for which user does not have control to the full underlying code (for example functions that call external libraries).
107	Apache Commons Math provides one implementation of the UnivariateFunctionDifferentiator interface: FiniteDifferencesDifferentiator .
108	This class creates a wrapper that will call the user-provided function on a grid sample and will use finite differences to compute the derivatives.
109	It takes care of boundaries if the variable is not defined on the whole real line.
110	It is possible to use more points than strictly required by the derivation order (for example one can specify an 8-points scheme to compute first derivative only).
111	However, one must be aware that tuning the parameters for finite differences is highly problem-dependent.
112	Choosing the wrong step size or the wrong number of sampling points can lead to huge errors.
113	Finite differences are also not well suited to compute high order derivatives.
114	Another implementation of the UnivariateFunctionDifferentiator interface is under development in the related project Apache Commons Nabla.
115	This implementation uses automatic code analysis and generation at binary level.
116	However, at time of writing (end 2012), this project is not yet suitable for production use.
117	Complex provides a complex number type that forms the basis for the complex functionality found in commons-math.
118	Complex functions and arithmetic operations are implemented in commons-math by applying standard computational formulas and following the rules for java.lang.Double arithmetic in handling infinite and NaN values.
119	No attempt is made to comply with ANSII/IEC C99x Annex G or any other standard for Complex arithmetic.
120	See the class and method javadocs for the Complex and ComplexUtils classes for details on computing formulas.
121	To create a complex number, simply call the constructor passing in two floating-point arguments, the first being the real part of the complex number and the second being the imaginary part:
122	Complex numbers may also be created from polar representations using the ComplexUtils.polar2Complex method in ComplexUtils .
123	The Complex class provides basic unary and binary complex number operations.
124	These operations provide the means to add, subtract, multiply and divide complex numbers along with other complex number functions similar to the real number functions found in java.math.BigDecimal:
125	Complex also provides implementations of serveral transcendental functions involving complex number arguments.
126	Prior to version 1.2, these functions were provided by ComplexUtils in a way similar to the real number functions found in java.lang.Math, but this has been deprecated.
127	These operations provide the means to compute the log, sine, tangent, and other complex values :
128	Complex instances can be converted to and from strings using the ComplexFormat class.
129	ComplexFormat is a java.text.Format extension and, as such, is used like other formatting objects (e.g. java.text.SimpleDateFormat):
130	To customize the formatting output, one or two java.text.NumberFormat instances can be used to construct a ComplexFormat .
131	These number formats control the formatting of the real and imaginary values of the complex number:
132	Another formatting customization provided by ComplexFormat is the text used for the imaginary designation.
133	By default, the imaginary notation is "i" but, it can be manipulated using the setImaginaryCharacter method.
134	Formatting inverse operation, parsing, can also be performed by ComplexFormat .
135	Parse a complex number from a string, simply call the ComplexFormat.parse method:
136	The distribution framework provides the means to compute probability density function (PDF) probabilities and cumulative distribution function (CDF) probabilities for common probability distributions.
137	Along with the direct computation of PDF and CDF probabilities, the framework also allows for the computation of inverse PDF and inverse CDF values.
138	Using a distribution object, PDF and CDF probabilities are easily computed using the AbstractIntegerDistribution.cumulativeProbability methods.
139	For a distribution X, and a domain value, x, AbstractIntegerDistribution.cumulativeProbability computes P(X <= x) (i.e. the lower tail probability of X).
140	The inverse PDF and CDF values are just as easily computed using the AbstractIntegerDistribution.inverseCumulativeProbability methods.
141	For a distribution X, and a probability, p, AbstractIntegerDistribution.inverseCumulativeProbability computes the domain value x, such that:
142	Since there are numerous distributions and Commons-Math only directly supports a handful, it may be necessary to extend the distribution framework to satisfy individual needs.
143	It is recommended that the Distribution, ContinuousDistribution, DiscreteDistribution, and IntegerDistribution interfaces serve as base types for any extension.
144	These serve as the basis for all the distributions directly supported by Commons-Math and using those interfaces for implementation purposes will ensure any extension is compatible with the remainder of Commons-Math.
145	To aid in implementing a distribution extension, the AbstractDistribution, AbstractContinuousDistribution, and AbstractIntegerDistribution provide implementation building blocks and offer basic distribution functionality.
146	By extending these abstract classes directly, much of the repetitive distribution implementation is already developed and should save time and effort in developing user-defined distributions.
147	The exceptions defined by Commons Math follow the Java standard hierarchies:
148	In all of the above exception hierarchies, several subclasses can exist, each conveying a specific underlying cause of the problem.
149	The detailed error messages (i.e. the string returned by the ExceptionContext.getLocalizedMessage method) can be localized.
150	However, besides the American/English default, French is the only language for which a translation resource is available.
151	Every exception generated by Commons Math implements the ExceptionContextProvider interface.
152	A call to the ExceptionContextProvider.getContext method will return the ExceptionContext instance stored in the exception, which the user can further customize by adding messages and/or any object.
153	KalmanFilter provides a discrete-time filter to estimate a stochastic linear process.
154	A Kalman filter is initialized with a ProcessModel and a MeasurementModel , which contain the corresponding transformation and noise covariance matrices.
155	The parameter names used in the respective models correspond to the following names commonly used in the mathematical literature:
156	Fraction and BigFraction provide fraction number type that forms the basis for the fraction functionality found in Commons-Math.
157	The former one can be used for fractions whose numerators and denominators are small enough to fit in an int (taking care of intermediate values) while the second class should be used when there is a risk the numerator and denominator grow very large.
158	A fraction number, can be built from two integer arguments representing numerator and denominator or from a double which will be approximated:
159	Of special note with fraction construction, when a fraction is created it is always reduced to lowest terms.
160	The Fraction class provides many unary and binary fraction operations.
161	These operations provide the means to add, subtract, multiple and, divide fractions along with other functions similar to the real number functions found in java.math.BigDecimal:
162	Like fraction construction, for each of the fraction functions, the resulting fraction is reduced to lowest terms.
163	Fraction instances can be converted to and from strings using the FractionFormat class.
164	FractionFormat is a java.text.Format extension and, as such, is used like other formatting objects (e.g. java.text.SimpleDateFormat):
165	To customize the formatting output, one or two java.text.NumberFormat instances can be used to construct a FractionFormat .
166	These number formats control the formatting of the numerator and denominator of the fraction:
167	Formatting's inverse operation, parsing, can also be performed by FractionFormat .
168	To parse a fraction from a string, simply call the FractionFormat.parse method:
169	GeneticAlgorithm provides an execution framework for Genetic Algorithms (GA).
170	Populations, consisting of Chromosomes are evolved by the GeneticAlgorithm until a StoppingCondition is reached.
171	Evolution is determined by SelectionPolicy , MutationPolicy and Fitness .
172	The GA itself is implemented by the GeneticAlgorithm.evolve method of the GeneticAlgorithm class, which looks like this:
173	Here is an example GA execution:
174	Interval and IntervalsSet represent one dimensional regions.
175	All classical set operations are available for intervals sets: union, intersection, symmetric difference (exclusive or), difference, complement, as well as region predicates (point inside/outside/on boundary, emptiness, other region contained).
176	It is also possible to compute geometrical properties like size, barycenter or boundary size.
177	Intervals sets can be built by constructive geometry (union, intersection ...) or from a boundary representation.
178	PolygonsSet represent two dimensional regions.
179	All classical set operations are available for polygons sets: union, intersection, symmetric difference (exclusive or), difference, complement, as well as region predicates (point inside/outside/on boundary, emptiness, other region contained).
180	It is also possible to compute geometrical properties like size, barycenter or boundary size and to extract the vertices.
181	Polygons sets can be built by constructive geometry (union, intersection ...) or from a boundary representation.
182	PolyhedronsSet represent three dimensional regions.
183	All classical set operations are available for polyhedrons sets: union, intersection, symmetric difference (exclusive or), difference, complement, as well as region predicates (point inside/outside/on boundary, emptiness, other region contained).
184	It is also possible to compute geometrical properties like size, barycenter or boundary size and to extract the vertices.
185	Polyhedrons sets can be built by constructive geometry (union, intersection ...) or from a boundary representation.
186	Vector3D provides a simple vector type.
187	One important feature is that instances of this class are guaranteed to be immutable, this greatly simplifies modelling dynamical systems with changing states: once a vector has been computed, a reference to it is known to preserve its state as long as the reference itself is preserved.
188	Numerous constructors are available to create vectors.
189	In addition to the straightforward cartesian coordinates constructor, a constructor using azimuthal coordinates can build normalized vectors and linear constructors from one, two, three or four base vectors are also available.
190	Constants have been defined for the most commons vectors (plus and minus canonical axes, null vector, and special vectors with infinite or NaN coordinates).
191	The generic vectorial space operations are available including dot product, normalization, orthogonal vector finding and angular separation computation which have a specific meaning in 3D.
192	The 3D geometry specific cross product is of course also implemented.
193	Vector3DFormat is a specialized format for formatting output or parsing input with text representation of 3D vectors.
194	Rotation represents 3D rotations.
195	Rotation instances are also immutable objects, as Vector3D instances.
196	Rotations can be represented by several different mathematical entities (matrices, axe and angle, Cardan or Euler angles, quaternions).
197	This class presents a higher level abstraction, more user-oriented and hiding implementation details.
198	Well, for the curious, we use quaternions for the internal representation.
199	The user can build a rotation from any of these representations, and any of these representations can be retrieved from a Rotation instance (see the various constructors and getters).
200	In addition, a rotation can also be built implicitely from a set of vectors and their image.
201	These examples show that a rotation means what the user wants it to mean, so this class does not push the user towards one specific definition and hence does not provide methods like projectVectorIntoDestinationFrame or computeTransformedDirection.
202	It provides simpler and more generic methods: Rotation.applyTo(Vector3D) and Rotation.applyInverseTo(Vector3D) .
203	Since a rotation is basically a vectorial operator, several rotations can be composed together and the composite operation r = r1 o r2 (which means that for each vector u, r(u) = r1(r2(u))) is also a rotation.
204	Hence we can consider that in addition to vectors, a rotation can be applied to other rotations as well (or to itself).
205	With our previous notations, we would say we can apply r1 to r2 and the result we get is r = r1 o r2.
206	For this purpose, the class provides the methods: Rotation.applyTo(Rotation) and Rotation.applyInverseTo(Rotation) .
207	BSP trees are an efficient way to represent space partitions and to associate attributes with each cell.
208	Each node in a BSP tree represents a convex region which is partitioned in two convex sub-regions at each side of a cut hyperplane.
209	The root tree contains the complete space.
210	The main use of such partitions is to use a boolean attribute to define an inside/outside property, hence representing arbitrary polytopes (line segments in 1D, polygons in 2D and polyhedrons in 3D) and to operate on them.
211	Another example would be to represent Voronoi tesselations, the attribute of each cell holding the defining point of the cell.
212	The RealMatrix interface represents a matrix with real numbers as entries.
213	The following basic matrix operations are supported:
214	Example:
215	The three main implementations of the interface are Array2DRowRealMatrix and BlockRealMatrix for dense matrices (the second one being more suited to dimensions above 50 or 100) and SparseRealMatrix for sparse matrices.
216	The RealVector interface represents a vector with real numbers as entries.
217	The following basic matrix operations are supported:
218	The RealVectorFormat class handles input/output of vectors in a customizable textual format.
219	The DecompositionSolver.solve() methods of the DecompositionSolver interface support solving linear systems of equations of the form AX=B, either in linear sense or in least square sense.
220	A RealMatrix instance is used to represent the coefficient matrix of the system.
221	Solving the system is a two phases process: first the coefficient matrix is decomposed in some way and then a solver built from the decomposition solves the system.
222	This allows to compute the decomposition and build the solver only once if several systems have to be solved with the same coefficient matrix.
223	For example, to solve the linear system
224	Each type of decomposition has its specific semantics and constraints on the coefficient matrix as shown in the following table.
225	For algorithms that solve AX=B in least squares sense the value returned for X is such that the residual AX-B has minimal norm.
226	If an exact solution exist (i.e. if for some X the residual AX-B is exactly 0), then this exact solution is also the solution in least square sense.
227	This implies that algorithms suited for least squares problems can also be used to solve exact problems, but the reverse is not true.
228	It is possible to use a simple array of double instead of a RealVector .
229	In this case, the solution will be provided also as an array of double.
230	It is possible to solve multiple systems with the same coefficient matrix in one method call.
231	To do this, create a matrix whose column vectors correspond to the constant vectors for the systems to be solved and use DecompositionSolver.solve(RealMatrix), which returns a matrix with column vectors representing the solutions.
232	Decomposition algorithms may be used for themselves and not only for linear system solving.
233	This is of prime interest with eigen decomposition and singular value decomposition.
234	The getEigenvalue(), getEigenvalues(), getEigenVector(), EigenDecomposition.getV() , EigenDecomposition.getD() and EigenDecomposition.getVT() methods of the EigenDecomposition interface support solving eigenproblems of the form AX = lambda X where lambda is a real scalar.
235	The SingularValueDecomposition.getSingularValues() , SingularValueDecomposition.getU() , SingularValueDecomposition.getS() and SingularValueDecomposition.getV() methods of the SingularValueDecomposition interface allow to solve singular values problems of the form AXi = lambda Yi where lambda is a real scalar, and where the Xi and Yi vectors form orthogonal bases of their respective vector spaces (which may have different dimensions).
236	In addition to the real field, matrices and vectors using non-real field elements can be used.
237	The fields already supported by the library are:
