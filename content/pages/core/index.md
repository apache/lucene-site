Title: Apache Lucene Core
URL: core/index.html
save_as: core/index.html
theme: lucene-core
template: lucene/core/page

Apache Lucene™ is a
high-performance, full-featured search engine library written entirely in Java.
It is a technology suitable for nearly any application that requires structured
search, full-text search, faceting, nearest-neighbor search across
high-dimensionality vectors, spell correction or query suggestions.

Apache Lucene is an open source project available for free download. Please use the
links on the right to access Lucene.

# Lucene™ Features

Lucene offers powerful features through a simple API:

## Scalable, High-Performance Indexing

- over [800GB/hour on modern hardware][1]
- small RAM requirements -- only 1MB heap
- incremental indexing as fast as batch indexing
- index size roughly 20-30% the size of text indexed

## Powerful, Accurate and Efficient Search Algorithms

- ranked searching -- best results returned first
- many powerful query types: phrase queries, wildcard queries, proximity
  queries, range queries and more
- fielded searching (e.g. title, author, contents)
* nearest-neighbor search for high-dimensionality vectors
- sorting by any field
- multiple-index searching with merged results
- allows simultaneous update and searching
- flexible faceting, highlighting, joins and result grouping
- fast, memory-efficient and typo-tolerant suggesters
- pluggable ranking models, including the [Vector Space Model][2] and [Okapi BM25][3]
- configurable storage engine (codecs)

Search performance of Apache Lucene is tracked in muliple places. Check out

 * [Mike McCandless' nightly benchmarks for Lucene](https://benchmarks.mikemccandless.com/) for an historical view of Lucene's query performance, going back to 2011 for some queries
 * [Search Benchmark, the Game](https://tantivy-search.github.io/bench/) for a comparison of Lucene with other search engines


## Cross-Platform Solution

- Available as Open Source software under the [Apache License][4] which lets you use
  Lucene in both commercial and Open Source programs
- 100%-pure Java
- Implementations [in other programming languages available][5]

[1]: https://benchmarks.mikemccandless.com/indexing.html
[2]: http://en.wikipedia.org/wiki/Vector_Space_Model
[3]: http://en.wikipedia.org/wiki/Okapi_BM25
[4]: https://www.apache.org/licenses/LICENSE-2.0.html
[5]: https://cwiki.apache.org/confluence/display/lucene/LuceneImplementations
