Title: Apache Lucene™ 10.5.0 available
category: core/news
URL:
save_as:

The Lucene PMC is pleased to announce the release of Apache Lucene 10.5.0.

Apache Lucene is a high-performance, full-featured search engine library written entirely in Java. It is a technology suitable for nearly any application that requires structured search, full-text search, faceting, nearest-neighbor search across high-dimensionality vectors, spell correction or query suggestions.

This release contains numerous bug fixes, optimizations, and improvements, some of which are highlighted below. The release is available for immediate download at:

  <https://lucene.apache.org/core/downloads.html>

### Lucene 10.5.0 Release Highlights:

 * A new experimental columnar batch indexing API
 * Improvements to bulk scoring and filtering of documents allowing much greater use of SIMD instructions and vectorisation
 * Extension of concurrent searches to many more Collector types, notably Grouping searches
 * New queries allowing hybrid searches to use Bayesian probabilities to combine scores from different index types (eg BM25 and vector scores)

Please read CHANGES.txt for a full list of new features and changes:

  <https://lucene.apache.org/core/10_5_0/changes/Changes.html>
