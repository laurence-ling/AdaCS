1	Fills virtual 'start' arc, ie, an empty incoming arc to the FST's start node
2	Appends a single suggestion and its weight to the internal buffers
3	It returns no mapping for query terms that occurs in a position insensitive way which therefore don't need to be filtered.
4	Replaces the current taxonomy with the given one
5	does NOT update term statistics.
6	is used to indicate that docs should be sorted by score.
7	Count the vowels in the string, we always require at least one in the remaining stem to accept it.
8	Performs lookup in transitions, assuming determinism.
9	Called whenever the running merges have changed, to set merge IO limits
10	Rebuild a phrase query with a slop value
11	a set to copy matchVersion will be of the given set will be preserved.
12	if any int value is out of bounds for a byte.
13	Translates a frozen packet of delete termquery, or doc values updates, into their actual docIDs in the index, and applies the change
14	init most recent DocValues for the current commit
15	Pulls CopyState off the wire
16	BytesReader, initial and scratch Arc, and result.
17	Compares a to b, returning less than 0, 0, or greater than 0, if a is less than, equal to, or greater than b, respectively, up to their common prefix (i.e
18	Normalize an input buffer of Arabic text
19	can be a comma-separated list of filenames
20	Construct a single array from a number of individual arrays.
21	Write an int to a stream.
22	IncRef the current CopyState and return it
23	The factory  is looked up via "prefixTree" in args, expecting "geohash" or "quad"
24	Convert Lucene wildcard syntax into an automaton.
25	Clear array and switch to new reader.
26	Simple command-line based search demo.
27	Each node stores a character (splitchar) which is part of some key(s)
28	Enumerates all minimal prefix paths in the automaton that also intersect the FST, accumulating the FST end node and output for each path.
29	Creates an edge interval tree from a set of polygon vertices.
30	Record intersection points for planes with error bounds
31	Runs the search example and prints the results.
32	a null termPart means it's a simple slice of the original term
33	Writes a codec header, which records both a string to identify the file and a version number
34	Remove the CommitPoints in the commitsToDelete List by
35	put the entry in map
36	index of a pp2 colliding with pp, or -1 if none
37	Removes the given number of byte blocks from the buffer if possible
38	Add a [virtual] epsilon transition between source and dest
39	invariant for document update
40	Find the intersection points between two planes, given a set of bounds.
41	Auto-completes a given prefix query using Depth-First Search with the end of prefix as source node each time finding a new leaf to get a complete key to be added in the suggest list
42	Called while highlighting a single result, to append a matched prefix token, to the provided fragments list
43	Calculate the latitude of a circle's intersections with its bbox meridians
44	Confirms that the incoming index sort (if any) matches the existing index sort (if any)
45	Flushes a bigram token to output from our buffer
46	Writes a file containing a JFlex macro that will accept any of the given
47	Utility method to check if some class loader is a (grand-)parent of or the same as another one
48	Determinizes the given automaton
49	Parses a specific affix rule putting the result into the provided affix map pattern
50	Expert: called to re-write queries into primitive queries.
51	Creates a new int slice with the given starting size and returns the slices offset in the pool.
52	Contains user EOF-code, which will be executed exactly once, when the end of file is reached
53	unmodifiable views of internal map for "read-only" use
54	Merges the readers into the directory passed to the constructor
55	non-comment initial line, either: 1
56	Run the quality benchmark
57	init most recent FieldInfos for the current commit
58	Creates complex phrase query from the cached tokenstream contents
59	Stems a word contained in a leading portion of a char[] array
60	Converts a long value into a full 64 bit string (useful for debugging)
61	(has depth &gt; 1 paths).
62	Obtain the current reference
63	Called when the primary changed
64	Does fininishing for a merge, which is fast but holds the synchronized lock on IndexWriter instance.
65	Draws a line a fixed latitude, spanning the minmax longitude
66	Does in-place XOR of the bits provided by the iterator.
67	Add a new transition with the specified source, dest, min, max.
68	spaces or other funky characters are detected.
69	Lookup suggestions sorted by weight (descending order)
70	mark the end of a task
71	Helper method to parse an XML file into a DOM tree, given a reader.
72	Writes the buffered skip lists to the given output.
73	Given an IndexSearcher, returns a new IndexSearcher whose IndexReader is a MultiReader containing the Reader of the original IndexSearcher, as well as several "empty" IndexReaders -- some of which will have deleted documents in them
74	of bits per value and format.
75	Load a stemmer table from an inputstream.
76	The original lexicon puts all information with punctuation into a chart (from 1 to 3755)
77	entries are passed to the Pruner in sorted (newest to oldest IndexSearcher) order
78	Compute the length of the next run, make the run sorted and return its length.
79	Allocates a new slice from the given offset
80	Mark that a task is starting
81	Calendar utility method: Gets the Calendar field code of the last field that is set prior to an unset field
82	Tests that a query matches the an expected set of documents using a
83	Iterates to the next script run, returning true if one exists.
84	Highlights the top-N passages from multiple fields, for the provided int[] docids
85	with repeats: not so simple.
86	Constructs a query to retrieve documents that are disjoint to the input envelope.
87	Make an effort to visit "fake" (e.g
88	decodes the contexts at the current position
89	Iterates all words parts and concatenations, buffering up the term parts we should return.
90	strings in UTF-8
91	Changes the values of the field
92	Compares 2 null terminated char arrays
93	Transitively resolves all dependencies in the given ivy.xml file, looking for indirect dependencies with versions that conflict with those of direct dependencies
94	Normalizes a Japanese number
95	Encode InetAddress value into binary encoding
96	transition leaving the specified state.
97	Initializes the reader, for reuse on a new term.
98	find the longest op name out of completed tasks.
99	Builds a Polygon2D from multipolygon
100	User runs a query and counts facets only without collecting the matching documents.
101	sugar encodes a single point as a byte array, rounding values up
102	Parses a pair of large numbers, i.e
103	shifting to the right if the window was previously full.
104	Constructs sub-automaton corresponding to decimal numbers of length x.substring(n).length().
105	Constructs sub-automaton corresponding to decimal numbers of value at least x.substring(n) and length x.substring(n).length().
106	folds single character (according to LANG if present)
107	Do an iota of work; returns true if all copying is done
108	TokenStream}, and creates the corresponding automaton where arcs are bytes (or Unicode code points if unicodeArcs = true) from each term.
109	term, with control over whether freqs are required
110	Advance tail to the lead until there is a match.
111	Converts either a compile output directory or an internal jar dependency, taken from an Ant (test.)classpath, into an artifactId
112	Compute linear distance from plane to a vector
113	Computes the full file name from base, extension and generation
114	Determine whether the plane intersects another plane within the bounds provided.
115	Removes the given number of int blocks from the buffer if possible
116	Removes a particle denotion ("ge") from a term.
117	Instantiate a serializable object from a stream.
118	passing an unexpected exception that has already occurred
119	Compute a GeoPoint that's a bisection between two other GeoPoints.
120	Initialize the provided Transition to iterate through all transitions get each transition
121	Create a predicate that checks whether points are within a distance of a given point
122	Parse large kanji numerals (ten thousands or larger)
123	A query time join using global ordinals over a dedicated join field
124	caches documents and scores up to the specified RAM threshold
125	Creates a span near (phrase) query from a graph token stream
126	Read hyphenation patterns from an XML file.
127	Allocates a new slice with the given size.
128	Advance to the next subword in the string.
129	User drills down on 'Publish Date2010', and we return facets for 'Author'
130	Creates CT (changed term) , substituting  'ã' and 'õ' for 'a~' and 'o~'.
131	Creates tree from sorted components (with range low and high inclusive)
132	Updates documents' DocValues fields to the given values
133	corresponding Calendar that is cleared below its level.
134	lookahead for a combining dot above
135	Absolute writeBytes without changing the current position
136	Compute a normalized unit vector based on the current vector
137	Parses a query stylesheet for repeated use
138	Checks a term if it can be processed correctly.
139	Create a sampled of the given hits.
140	Serialize the token data for communication between server and client.
141	Concatenate the buffers in any order, leaving at least one empty slot in the end
142	Adds terms and frequencies found in vector into the Map termFreqMap
143	Helper method that reads CFS entries from an input stream
144	Expert: Set a new reader on the Tokenizer
145	Called from processDocument to index one field's point
146	Create the More like query from a PriorityQueue
147	Used when drill downs are highly constraining vs baseQuery.
148	Quote and escape input value for CSV
149	Absolute copy bytes self to self, without changing the position
150	Sort input to a new temp file, returning its name.
151	Delete all documents in the index
152	Construct a patch string that transforms a to b.
153	Creates a query from a token stream.
154	Decodes the Unicode codepoints from the provided
155	perform a logical and of 2 QueryNode trees
156	Replace a string suffix by another
157	Convenience method; Tokenizes the given field text and adds the resulting terms to the index; Equivalent to adding an indexed non-keyword Lucene termVectorStored with positions (or termVectorStored with positions and offsets), a name to be associated with the text the text to tokenize and index
158	Change (or set) the minmax values of the field.
159	Appends the current contents of writeBuffer as another block on the growing in-memory file
160	reader, merging fieldstermsdocspositions on the fly
161	If the word ends with one of ( e é ê) in RV,delete it, and if preceded by 'gu' (or 'ci') with the 'u' (or 'i') in RV, delete the 'u' (or 'i') Or if the word ends ç remove the cedilha
162	Cross check if declaring class of given method is the same as
163	Called once replica is done (or failed) copying an NRT point
164	if we need to tie-break since score  sort value are the same we first compare shard index (lower shard wins) and then iff shard index is the same we use the hit index.
165	Compute the minimum shift value so that
166	Splits file names separated by comma character
167	Break the given patch command into its constituent pieces
168	Packs the two arrays, representing a balanced binary tree, into a compact byte[] structure.
169	Creates a SAX parser using JAXP
170	Recursive depth-first path search
171	Prunes the blockedQueue by removing all DWPT that are associated with the given flush queue.
172	Sugar to get all transitions for all states
173	accurate counts of the dimension, i.e
174	1) Turn to lowercase 2) Remove accents 3) ã -&gt; a ; õ -&gt; o 4) ç -&gt; c
175	Specialized getByOutput that can understand the ranges (startOrd to endOrd) we use here, not just startOrd.
176	Rough Linux-only heuristics to determine whether the provided returns false if the disk is a solid-state disk.
177	Locate a point that is within the specified bounds and on the specified plane, that has an arcDistance as specified from the startPoint.
178	Copy BytesRef in, setting BytesRef out to the result
179	Constructs sub-automaton corresponding to decimal numbers of value between x.substring(n) and y.substring(n) and of length x.substring(n).length() (which must be equal to y.substring(n).length()).
180	Build a FieldFragList for more than one field.
181	For each module, sets a compile-scope and a test-scope property with values that contain the appropriate &lt;dependency&gt; snippets.
182	Construct the most accurate normalized plane through an x-z point and including the Y axis
183	Balance the tree for best search performance
184	Finds the number of subsequent next iteration marks
185	Parse command line args into fields
186	Create a random instance.
187	Add the given mapping
188	Creates a specific FSDirectory instance starting from its class name
189	or if the field has no term vector, or if the term vector doesn't have offsets
190	Recursively finds indirect dependencies that have a version conflict with a direct dependency
191	Writes a codec header for an index file, which records both a string to identify the format of the file, a version number, and data to identify the file instance (ID and auxiliary suffix such as generation)
192	Flush all index operations to disk and opens a new near-real-time reader
193	Tests that all documents up to maxDoc which are not in the expected result set, have an explanation which indicates that the document does not match
194	fired when the max non-competitive boost has changed
195	Parses a string such as "Intersects(ENVELOPE(-10,-8,22,20)) distErrPct=0.025".
196	Maps a file into a set of buffers
197	Builds the final automaton from a list of entries.
198	Replace pattern in input and mark correction offsets.
199	Cache the root node's output arcs starting with completions with the highest weights.
200	except the input is in snowball format.
201	String compare, returns 0 if equal or t is a substring of s
202	Branches are initially compressed, needing one node per key plus the size of the string key
203	Calendar utility method: the remainder in an un-set state
204	Creates a minimum-should-match query from the query text
205	Just maps each UTF16 unit (char) to the ints in an
206	At initialization (each doc), each repetition group is sorted by (query) offset
207	Index all text files under a directory.
208	Expert: compares the bytes against another BytesRef, returning true if the bytes are equal.
209	Rounds down required maxNumberOfBits to the nearest number that is made up of all ones as a binary number
210	Override if you wish to change what is extracted
211	Reverses the automaton, returning the new initial states.
212	Removes and returns the least element of the PriorityQueue in log(size) time.
213	Clears a range of bits.
214	Stop the update thread
215	User drills down on 'Publish Date2010', and we return facets for both 'Publish Date' and 'Author', using DrillSideways.
216	Reverse from srcPos, inclusive, to destPos, inclusive.
217	Expert: Creates an array of leaf slices each holding a subset of the given leaves.
218	Read the class from the stream
219	Creates complex boolean query from the cached tokenstream contents
220	Collect external dependencies from the given ivy.xml file, constructing property values containing &lt;dependency&gt; snippets, which will be filtered (substituted) when copying the POM for the module corresponding to the given ivy.xml file.
221	Inserting keys in TST in the order middle,small,big (lexicographic measure) recursively creates a balanced tree which reduces insertion and search times significantly
222	Pushes all previously pop'd enums back into the docIDQueue
223	Create and return a new MergeThread
224	Used when base query is highly constraining vs the drilldowns, or when the docs must be scored at once (i.e., like BooleanScorer2, not BooleanScorer)
225	Freezes the last state, sorting and reducing the transitions.
226	Split source index into multiple parts
227	Create a geobbox of the right kind given the specified bounds.
228	Must be thread-safe.
229	Snapshots the last commit and returns it
230	Retrieve the next break position
231	Called to summarize a document when no highlights were found
232	Release a snapshot by generation.
233	Does the actual (time-consuming) work of the merge, but without holding synchronized lock on IndexWriter instance
234	Highlights terms in the  text , extracting the most relevant sections and concatenating the chosen fragments with a separator (typically "...")
235	Add a specific Z value.
236	Reinitializes head, freq and doc from 'head'
237	Stem a term (returning its new length)
238	Appends an updateDocument op
239	Create a XYZSolid of the right kind given (x,y,z) bounds.
240	Expert: attempts to delete by document ID, as long as
241	folds titlecase variant of word to titleBuffer
242	replace with ignore case string to get replaced the old character sequence in lowercase the new character to prefix sequence1 in return string.
243	Uses a hyperbolic tangent function that allows for a hard max..
244	Ask the primary node process to flush
245	If buffered deletes are using too much heap, resolve them and write disk and return true.
246	Stem a prefix off an Arabic word.
247	Explain the custom score
248	Deletes the document(s) containing any of the terms
249	Constructs a query to retrieve documents that intersect the input envelope.
250	Normalizes the iteration mark character c
251	Compute normal distance from plane to a vector.
252	User drills down on 'Publish Year2010'.
253	Reads a stem dictionary
254	Do a specific action and validate after the action that the status is still OK, and if not, attempt to extract the actual server side exception
255	Rewinds enum state to match the shared prefix between current term and target term
256	Increment the round number, for config values that are extracted by round number.
257	Create a query for matching a bounding box
258	Whether evictions are required.
259	Writes buffer to the file and returns the start position.
260	suffix stripping (stemming) on the current term
261	Remove all cache entries for the given core cache key.
262	if possible and configured.
263	Removes the calling thread from the active merge threads.
264	Pops all enums positioned on the current (minimum) doc
265	Do some substitutions for the term to reduce overstemming: "ß" is substituted by "ss" - Substitute a second char of a pair of equal characters with - Substitute some common character combinations with a token:
266	Compute the path type of a file by inspecting name of file and its parents
267	Build the suggest index, using up to the specified amount of temporary RAM while building
268	Normalize an input buffer of Persian text
269	Create a query for matching a bounding box using doc values
270	Create a prefix query for matching a CIDR network range.
271	Pick a random pole that has a good chance of being inside the polygon described by the points.
272	Find the points between two planes, where one plane crosses the other, given a set of bounds
273	Report detailed statistics as a string
274	Slower transformation using an uncompiled stylesheet (suitable for development environment)
275	Optimize (remove holes in the rows) the given Trie and return the restructured Trie.
276	Normalizes input text, and returns the new length
277	Copies over all statestransitions from other
278	Mainly remove the definite article
279	specify whether the call should block until the operation completes
280	will be returned, other times a aren't equal).
281	Insert an entry in 'tail' and evict the least-costly scorer if full.
282	Adds multiple vals to the Set associated with key in the Map
283	Parse a resource file into an RSLP stemmer description.
284	Recursivelly visists each node to calculate the number of nodes
285	Builds an extension field string from a given extension key and the extensions field
286	Checks if the word contained in the leading portion of char[] array , ends with the suffix given as parameter.
287	Instantiates the given analysis factory class after pulling params from the given stream tokenizer, then stores the result in the appropriate pipeline component list.
288	Convert Map of index and wordIdAndLength to array of {wordId, index, length}
289	Constructs a query to retrieve documents that equal the input envelope.
290	Create a QualityStats object that is the average of the input QualityStats objects.
291	Expert: returns a readonly reader, covering all committed as well as un-committed changes to the index
292	Reads a Set&lt;String&gt; previously written
293	Given a queue Entry, creates a corresponding FieldDoc that contains the values used to sort the given document
294	Check that the given index is good to use for block joins.
295	Checks whether there is a loop containing state
296	Draws a line a fixed longitude, spanning the minmax latitude
297	Safe (but, slowish) default method to write every vector field in the document.
298	Copy numBytes bytes from input to ourself.
299	Stem an input buffer of Bulgarian text.
300	union (term group) bit-sets until they are disjoint (O(n^^2)), and each group have different terms
301	map each term to the single group that contains it
302	Stem an input buffer of Sorani text.
303	Lookup words in text
304	Records a value in the set
305	Create a predicate that checks whether points are within a polygon.
306	refills buffers with new data from the current token.
307	Normalize an input buffer of Bengali text
308	Pushes CopyState on the wire
309	Utility: execute benchmark from command line
310	path is the "address" by keys of where we are, e.g
311	Collect transitive compile-scope dependencies for the given artifact's ivy.xml from the Ivy cache, using the default ivy pattern "[organisation][module]ivy-[revision].xml"
312	Run a vocabulary test against two data files.
313	Normalize an input buffer of Sorani text
314	Convert to lowercase in-place.
315	Called once per inverted token
316	If there is no searcher then we simply always return null.
317	number of elements common to both arrays (from the start of each).
318	Iterate to the next transition after the provided one
319	Parses the query text and returns parsed query
320	Removes an existing element currently stored in the PriorityQueue
321	Writes all the entries for the FST input term
322	Converts a hex string into an int
323	Tests that a query matches the an expected set of documents using Hits
324	Checks if a term could be stemmed.
325	For a specified point and a list of poly points, determine based on point order whether the point should be considered in or out of the polygon
326	into  modify the captured state.
327	encode the minmax range into the provided byte array
328	Create the coefficient to transform the weight.
329	Compute Bounding Box for a circle using WGS-84 parameters
330	Write header to the lines file - indicating how to read the file later.
331	Parses the string argument as if it was an int value and returns the result
332	Compute the relation between the provided box and distance query
333	Actually perform the index check
334	pp was just advanced
335	Converts the Calendar into a Shape
336	Creates a CharArraySet from a path
337	Loads the skip levels
338	Adds a new resolved (meaning it maps docIDs to new values) doc values packet
339	Compute a report line for the given task stat.
340	Run the task, record statistics.
341	Turns a dim + path into an encoded string.
342	Reads stopwords from a stopword list in Snowball format
343	Factory method to generate a prefix query.
344	sugar encodes a single point as a byte array
345	Slow means of constructing query parsing a stylesheet from an input stream
346	Provide spelling corrections based on several parameters.
347	Loads the String values for each docId by field to be highlighted
348	Stem a word contained in a portion of a char[] array
349	Allocates internal skip buffers.
350	Compares incoming per-file identity (id, checksum, header, footer) versus what we have locally and returns the subset of the incoming files that need copying
351	Builds the actual sliced IndexInput (may apply extra offset in subclasses).
352	For every number of bits per value, there is a minimum number of blocks (b)  values (v) you need to write in order to reach the next block boundary: - 16 bits per value -&gt; b=2, v=1 - 24 bits per value -&gt; b=3, v=1 - 50 bits per value -&gt; b=25, v=4 - 63 bits per value -&gt; b=63, v=8 - ..
353	Reverse lookup (lookup by output instead of by input), in the special case when your FSTs outputs are strictly ascending
354	Expert: directly set the maximum number of merge threads and simultaneous merges allowed
355	Factory method for generating a query
356	expert: writes a value dictionary for a sortedsortedset field
357	Appends a deleteDocuments op
358	Encode string into HTML
359	Inserts a key in TST creating a series of Binary Search Trees at each node
360	Construct a sided plane from two points and a third normal vector.
361	Expert: low-level implementation method
362	Adds val to the Set associated with key in the Map
363	form the highlighted snippets.
364	Retrieves the CharsetDecoder for the given encoding
365	Ensure that any writes to the given file is written to the storage device that contains it
366	Adapt all dependencies and evictions from the ResolveReport.
367	Extract module name from ivy.xml path.
368	Like getRecomputedSizeInBytes(), but, uses actual file lengths rather than buffer allocations (which are quantized up to nearest
369	Simulates a crash of OS or machine by overwriting unsynced files.
370	Deletes the document(s) matching any of the provided queries
371	Deletes the specified files, but only if they are new (have not yet been incref'd).
372	Peeks at next arc's label; does not alter arc
373	Runs the sum intfloat associations examples and prints the results.
374	Factory method for generating query, given a set of clauses
375	Wraps a multi-valued SortedSetDocValues as a single-valued view, using the specified selector
376	Reorder based on startend offsets for each bucket
377	"summarizing" its contents, is precisely the same file that we have locally
378	Determine the relationship between the GeoAreShape's edgepoints and the provided shape.
379	Reset the text to a new value, and reset all state
380	Provided for testing purposes
381	Adds term frequencies found by tokenizing text from reader into the Map words
382	For each artifact in the project, append a dependency with version ${project.version} to the grandparent POM's &lt;dependencyManagement&gt; section
383	Convenience routine to make it easy to return the most interesting words in a document.
384	algorithm is the fraction of the distance from the center of the query shape to its closest bounding box corner.
385	determines if the passed term is likely to be of interest in "more like" comparisons
386	Order the subSpans within the same document by using nextStartPosition on all subSpans after the first as little as necessary
387	For a given filter, return how many times it should appear in the history before being cached
388	Creates a CharArraySet from a file resource associated with a class
389	Write a new value
390	Converts the tokenStream to an automaton
391	Finds an arc leaving the incoming arc, replacing the arc in place
392	looks at next input token, returning false is none is available
393	Reads lines from a Reader and adds every non-comment line as an entry to a CharArraySet (omitting leading and trailing whitespace)
394	Run a vocabulary test against two data files inside a zip file
395	path} into an encoded string.
396	Stems the text in the token
397	Generates a wordnumber part, updating the appropriate attributes
398	can hold the requested number of bits
399	Writes an int as four bytes
400	Reads the affix file through the provided InputStream, building up the prefix and suffix maps
401	Skip the next block of data.
402	Repairs the index using previously returned result remove any of the unreferenced files after it's done; deletes unreferenced files when it's created
403	Constructs a compound token.
404	Accesses a resource by name and returns the (non comment) lines containing data using the given character encoding
405	Remove all cache entries for the given query.
406	Waits for all in-flight packets, which are already being resolved concurrently by indexing threads, to finish
407	Highlights the top-N passages from multiple fields
408	Test whether the given Row of Cells in a Trie should be included in an optimized Trie
409	specify whether the call should block until all merging completes
410	unmodifiable views of internal sets for "read-only" use
411	Score a candidate doc for all slop-valid position-combinations (matches) encountered while traversinghopping the PhrasePositions
412	Add the next inputoutput pair
413	Removes all terms from the spell check index.
414	Deinterleaves long value back to two concatenated 32bit values
415	Run a vocabulary test against one file: tab separated.
416	Compute surface distance between two points.
417	Compute a title line for a report table
418	If cache is full remove least recently used entries from cache
419	Check whether two Spans in the same document are ordered with possible overlap
420	Simple heuristics to try to avoid over-pruning potential suggestions by the
421	Decrefs all provided files, even on exception; throws first exception hit, if any.
422	Writes an int at the absolute position without changing the current pointer.
423	Expert: just reads and verifies the object ID of an index header
424	Combine original user data with the taxonomy epoch.
425	Adds a "arbitrary" int offset instead of a BytesRef term
426	Read a PlanetObject from a stream.
427	the state of the index
428	Check a single ivy.xml file for dependencies' versions in rev="${orgname}" format
429	Find the unique stem(s) of the provided word
430	Adds clauses generated from analysis over text containing whitespace
431	Improves readability of a score-sorted list of TextFragments by merging any fragments that were contiguous in the original text into one larger fragment with the correct order
432	Parses the sourceText into an ANTLR 4 parse tree
433	count the number of documents in the index having at least a value for the 'class' field
434	Create a conjunction over the provided DocIdSetIterators
435	compare two arrays starting at the specified offsets.
436	Write a class to a stream.
437	Cleans up the index directory from old index files
438	at the end of the stream.
439	Decodes the Unicode codepoints from the provided char[] and places them in the provided scratch
440	Report a search result for a certain quality query.
441	Advance all entries from the tail to know about all matches on the current doc.
442	Fast means of constructing query using a precompiled stylesheet
443	Determine the offset source for the specified field
444	reader, merging live Documents on the fly
445	Copy another chunk of bytes, returning true once the copy is done
446	Blocks if documents writing is currently in a stalled state.
447	Compute the angle for a point given rotation information.
448	Parses a normalized javascript variable
449	Removes all entries from the PriorityQueue.
450	Encodes doc into buffer
451	Merge the given Cells and return the resulting Cell
452	Does in-place OR of the bits provided by the iterator
453	Check if foldToASCII generated a different token.
454	using the leaf reader's ordinal
455	Determines the amount of RAM that may be used for buffering added documents and deletions before they are flushed to the Directory
456	Initialize PhrasePositions in place
457	Finalize the automaton and return the root state
458	Add a specific Y value.
459	encodes an entry (bytes+(contexts)+(payload)+weight) to the provided writer
460	Constructs a query to retrieve documents are fully within the input envelope.
461	Normalize an input buffer of Hindi text
462	Compute arc distance from plane to a vector.
463	Commits final byte[], trimming it if necessary and if trim=true
464	Find the nth word in the dictionary that starts with the supplied prefix
465	Compare two arrays, starting at the specified offsets, but treating shortArray as a prefix to longArray
466	Merge the given rows and return the resulting Row
467	decodes the weight at the current position
468	Calculate the weight coefficient based on the position of the first matching word
469	Deletes all given file names
470	Add the given key associated with the given patch command
471	Factory method to generate a standard query (no phrase or prefix operators).
472	decodes the payload at the current position
473	Compares a string with null terminated char array
474	Read in a single partition of data, setting isExhausted[0] to true if there are no more items.
475	Creates a StorableField whose value will be lazy loaded if and when it is used
476	Recursivelly vists the nodes in order to find the ones that almost match a given key
477	Parses the encoding specified in the affix file readable through the provided InputStream
478	Merges an array of TopGroups, for example obtained from the second-pass collector across multiple shards
479	Converts a sequence of Java characters to a sequence of unicode code points.
480	A hook for extending classes to close additional resources that were used
481	find repeating terms and assign them ordinal values
482	Expert: add a custom drill-down subQuery
483	Downloads the IANA Root Zone Database.
484	Computes the type of the given character
485	Undoes the changes made by substitute()
486	Called when another node (replica) wants to copy files from us
487	Accumulate values of the histogram so that it does not store counts but
488	Generates a non-cryptographic globally unique id.
489	Parses a Japanese number
490	Parses a pair of "medium sized" numbers, i.e
491	Iterate through the failures list, giving each object a chance to throw an IOE
492	Construct the most accurate normalized plane through an y-z point and including the X axis
493	Creates a new byte slice with the given starting size and returns the slices offset in the pool.
494	Determine the relationship between the GeoAreaShape's edgepoints and the provided shape.
495	Called by indexing threads once they are fully done resolving all deletes for the provided delGen
496	Buffers the current input token into lookahead buffer.
497	Writes the current skip data to the buffers
498	no repeats: simplest case, and most common
499	Check Method signature for compatibility.
500	User drills down on 'tagssolr'.
501	Provides information on which stop words have been identified for all fields
502	Compute new point given original point, a bearing direction, and an adjusted angle (as would be computed by the surfaceDistance() method above)
503	Estimates a "shallow" memory usage of the given object
504	Factory method to generate a phrase query with slop.
505	Create a PriorityQueue from a word-&gt;tf map.
506	Reads lines from a Reader and adds every line as an entry to a CharArraySet (omitting leading and trailing whitespace)
507	Creates simple boolean query from the cached tokenstream contents
508	Concatenates the saved buffer to the given WordDelimiterConcatenation
509	Executes the replication task.
510	checks condition of the concatenation of two strings
511	Create a GeoPolygon using the specified points and holes, using order to determine siding of the polygon
512	Called from processDocument to index one field's doc value
513	Builds and stores a FST that can be loaded with
514	Find points on the boundary of the intersection of a plane and the unit sphere, given a starting point, and ending point, and a list of proportions of the arc (e.g
515	Neither array is modified.
516	has no trailing 'Z', and will be truncated to the units given according to
517	Normalize a string down to the representation that it would have in the index
518	Read quality queries from trec format topics file.
519	Determine whether the plane crosses another plane within the bounds provided
520	Called if we hit an exception at a bad time (when updating the index files) and must discard all currently buffered docs
521	Find the stem(s) of the provided word
522	Builds a new GraphQuery for multi-terms synonyms
523	For each module that includes other modules' external dependencies via including all files under their "...lib" dirs in their (test.)classpath, add the other modules' dependencies to its set of external dependencies.
524	Creates new buffers or empties the existing ones
525	Counts directly from SortedNumericDocValues.
526	Wait for any currently outstanding merges to finish
527	Factory method for generating a query (similar to token that uses prefix notation; that is, contains a single '' wildcard character as its last character
528	Determines whether the transition from lastType to type indicates a break
529	Constructs sub-automaton corresponding to decimal numbers of value at most x.substring(n) and length x.substring(n).length().
530	Only used by IW.rollback
531	Compiles the given expression with the specified parent classloader
532	at least one indexed document
533	Recursively prints stats for all ordinals.
534	initialize with checking for repeats
535	bit-sets - for each repeating pp, for each of its repeating terms, the term ordinal values is set
536	Parses "a=b c=d f" (whitespace separated) into name-value pairs
537	Internal recursive traversal for conversion.
538	Derives configuration conflicts that exist between node and all of its descendant dependencies.
539	Read values that have been written using variable-length encoding instead of bit-packing.
540	encodes a two-dimensional geo bounding box into a byte array
541	Subclass can override to customize per-dim Facets impl.
542	Parse the given version number as a constant or dot based version.
543	Tunes IO throttle when a new merge starts.
544	Re-initialize the state
545	Read the next value.
546	Note: Document instance is re-used per-thread
547	Steals incoming infos refCount; returns true if there were changes.
548	a map to copy matchVersion will be of the given map will be preserved.
549	Write dictionary in file
550	Reduce the trie using Lift-Up reduction
551	Does initial setup for a merge, which is fast but holds the synchronized lock on IndexWriter instance.
552	Append a new long.
553	Computes the number of intervals (rows or columns) to cover a range given the sizes.
554	Helper method, to deal with onOpen() throwing exception
555	Creates simple term query from the cached tokenstream contents
556	Merges the given taxonomy and index directories and commits the changes to the given writers.
557	is contained in a single block in the byte block pool.
558	Parse medium kanji numerals (tens, hundreds or thousands)
559	Compiles the given expression with the supplied custom functions
560	Reads a Map&lt;String,String&gt; previously written
561	Creates a span query from the tokenstream
562	Create the results based on the search hits
563	Writes the joined unhyphenated term
564	Recursively insert the median first and then the median of the lower and upper halves, and so on in order to get a balanced tree
565	Stem suffix(es) off an Arabic word.
566	one value per document.
567	Add a (possibly relevant) doc.
568	Parses a "medium sized" number, typically less than 10,000（万）, but might be larger due to a larger factor from {link parseBasicNumber}.
569	Flushes all indexing ops to disk and notifies all replicas that they should now copy
570	Pop the least-costly scorer from 'tail'.
571	Find the shortest path with the Viterbi algorithm.
572	Converts a sequence of unicode code points to a sequence of Java characters.
573	Hyphenate word and return an array of hyphenation points
574	Read quality queries from trec 1MQ format topics file.
575	Parses [[lat, lon], [lat, lon] ...] into 2d double array
576	thread when there are too many merges running or pending
577	Pick the next dimension to split.
578	Suggest similar words (optionally restricted to a field of an index)
579	field and term, with control over whether offsets and payloads are required
580	Creates a multifield query
581	Writes a close approximation to the parsed input format.
582	Deletes one or more files or directories (and everything underneath it)
583	Converts an incoming utf32 automaton to an equivalent utf8 one
584	Tests that a Hits has an expected order of documents
585	Minimizes (and determinizes if not already deterministic) the given automaton using Hopcroft's algorighm
586	Form all ngrams for a given word.
587	Perform non-recursive Ant-like property value interpolation
588	Recursively visits each node to be deleted
589	Start the update thread with the specified interval in milliseconds
590	Stem a latvian word
591	Construct the most accurate normalized plane through an x-y point and including the Z axis
592	Removes transitions to dead states (a state is "dead" if it is not reachable from the initial state or no accept state is reachable from it.)
593	Creates tree from sorted edges (with range low and high inclusive)
594	Waits for the target generation to become visible in the searcher, up to a maximum specified milli-seconds
595	Reset inputs so that the test run would behave, input wise, as if it just started.
596	Factory method to generate a fuzzy query.
597	Constructs a query to retrieve documents that do or do not cross the date line and match the supplied spatial query.
598	merge requested by the MergePolicy
599	Acquires write locks on all the directories; be sure finally clause.
600	Creates and returns a searcher that can be used to execute arbitrary
601	Create a large GeoPolygon
602	Obtain the number of deleted docs for a pooled reader
603	Add a specific X value.
604	Indexes a single document
605	Flushes a unigram token to output from our buffer
606	Create a new Pair
607	Highlights chosen terms in a text, extracting the most relevant sections
608	Appends an addDocument op
609	Limit a date's resolution
610	Look up the text string corresponding with the word char array, and return the position of the word list
611	Creates simple phrase query from the cached tokenstream contents
612	Compute the longitude for the point.
613	Instantiate a serializable object from a stream without a planet model.
614	Just converts IntsRef to BytesRef; you must ensure the int values fit into a byte.
615	Fills counts corresponding to the original input ranges, returning the missing count (how many hits didn't match any ranges).
616	Rebuilds a boolean query and sets a new minimum number should match value.
617	Collects indirect dependency version conflicts to ignore in ivy-ignore-conflicts.properties, and also checks for orphans (coordinates not included in ivy-versions.properties)
618	Stem an input buffer of Czech text
619	escape all tokens that are part of the parser syntax on a given string string to get replaced locale to be used when performing string compares
