Title: Apache Lucene™ 10.5.1 available
category: core/news
URL:
save_as:

The Lucene PMC is pleased to announce the release of Apache Lucene 10.5.1.

Apache Lucene is a high-performance, full-featured search engine library written entirely in Java. It is a technology suitable for nearly any application that requires structured search, full-text search, faceting, nearest-neighbor search across high-dimensionality vectors, spell correction or query suggestions.

This release contains numerous bug fixes, optimizations, and improvements, some of which are highlighted below. The release is available for immediate download at:

  <https://lucene.apache.org/core/downloads.html>

### Lucene 10.5.1 Release Highlights:


  * Fixed DocValuesRangeIterator.docIDRunEnd() returning wrong run boundaries, which could cause bulk-scoring toskip or mis-score documents in range and ordinal set queries 

  * Restored HNSW graph reuse during merges with per-field vector formats (including the default codec). 

  * HNSW graph construction now checks periodically whether the surrounding merge was aborted, so IndexWriter#rollback() and abortMerges() no longer block until the full graph is built. 

  * Fixed scoring on scalar-quantized indexes after raw float vectors were dropped; FloatVectorValues#scorer now scores against quantized vectors, matching behavior when raw vectors are present.

Please read CHANGES.txt for a full list of changes:

  <https://lucene.apache.org/core/10_5_1/changes/Changes.html>