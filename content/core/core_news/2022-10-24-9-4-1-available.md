Title: Apache Lucene™ 9.4.1 available
category: core/news
URL:
save_as:

The Lucene PMC is pleased to announce the release of Apache Lucene 9.4.1.

Apache Lucene is a high-performance, full-featured search engine library written entirely in Java. It is a technology suitable for nearly any application that requires structured search, full-text search, faceting, nearest-neighbor search across high-dimensionality vectors, spell correction or query suggestions.

This release contains numerous bug fixes, optimizations, and improvements, some of which are highlighted below. The release is available for immediate download at:

  <https://lucene.apache.org/core/downloads.html>

### Lucene 9.4.1 Release Highlights:

 * When reading large segments, the kNN vectors format could fail with a validation error, preventing further writes or searches on the index. This bug is now fixed. Only version 9.4.0 was affected, so it is recommended to skip 9.4.0 if you are using kNN vectors.

Please read CHANGES.txt for a full list of changes:

  <https://lucene.apache.org/core/9_4_1/changes/Changes.html>
