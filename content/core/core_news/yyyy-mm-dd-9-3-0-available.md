Title: Apache Lucene™ 9.3.0 available
category: core/news
URL:
save_as:

The Lucene PMC is pleased to announce the release of Apache Lucene 9.3.0.

Apache Lucene is a high-performance, full-featured search engine library written entirely in Java. It is a technology suitable for nearly any application that requires structured search, full-text search, faceting, nearest-neighbor search across high-dimensionality vectors, spell correction or query suggestions.

This release contains numerous bug fixes, optimizations, and improvements, some of which are highlighted below. The release is available for immediate download at:

  <https://lucene.apache.org/core/downloads.html>

### Lucene 9.3.0 Release Highlights:

 * Merge on full flush is enabled now by default with a timeout of 500ms, giving the merge policy a chance to merge NRT segments together before publishing a new point-in-time view of the IndexReader. This should give queries a small performance boost in the near-realtime case, especially terms-dictionary-intensive queries like fuzzy queries.
 * Add getAllChildren functionality to facets.
 * Added facetsets module for high dimensional (hyper-rectangle) faceting. 
 * Top-level two-clause disjunctions sorted by score now use the block-max MAXSCORE algorithm, which introduced a 40%-75% speedup in our benchmarks.
 * BooleanQuery can return quick counts for simple boolean queries.
 * When running KnnVectorQuery with a filter, reuse the cached filter bit set.

Please read CHANGES.txt for a full list of new features and changes:

  <https://lucene.apache.org/core/9_3_0/changes/Changes.html>
