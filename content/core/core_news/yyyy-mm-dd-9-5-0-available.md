Title: Apache Lucene™ 9.5.0 available
category: core/news
URL:
save_as:

The Lucene PMC is pleased to announce the release of Apache Lucene 9.5.0.

Apache Lucene is a high-performance, full-featured search engine library written entirely in Java. It is a technology suitable for nearly any application that requires structured search, full-text search, faceting, nearest-neighbor search across high-dimensionality vectors, spell correction or query suggestions.

This release contains numerous bug fixes, optimizations, and improvements, some of which are highlighted below. The release is available for immediate download at:

  <https://lucene.apache.org/core/downloads.html>

### Lucene 9.5.0 Release Highlights:

#### New features

 * Added KnnByteVectorField and ByteVectorQuery that are specialized for indexing and querying byte-sized vectors. Deprecated KnnVectorField, KnnVectorQuery and LeafReader#getVectorValues in favour of the newly introduced KnnFloatVectorField, KnnFloatVectorQuery and LeafReader#getFloatVectorValues that are specialized for float vectors.
 * Added IntField, LongField, FloatField and DoubleField: easy to use numeric fields that perform well both for filtering and sorting.
 * Support for Java 19 foreign memory access ("project Panama") was enabled by default removing the need to provide the "--enable-preview" flag.
 * Added ByteWritesTrackingDirectoryWrapper to expose metrics for bytes merged, flushed, and overall write amplification factor.

#### Optimizations

* Improved storage efficiency of connections in the HNSW graph used for vector search
* Added  new stored fields and term vectors interfaces: IndexReader#storedFields and IndexReader#termVectors. These do not rely upon ThreadLocal storage for each index segment, which can greatly reduce RAM requirements when there are many threads and/or segments.
* Several improvements were made to IndexSortSortedNumericDocValuesRangeQuery including query execution optimization with points for descending sorts and BoundedDocIdSetIterator construction sped up using bkd binary search.
S
#### Other

* Moved DocValuesNumbersQuery from sandbox to NumericDocValuesField#newSlowSetQuery
* Fix exponential runtime for nested BooleanQuery#rewrite with non scoring clauses

Please read CHANGES.txt for a full list of new features and changes:

  <https://lucene.apache.org/core/9_5_0/changes/Changes.html>
