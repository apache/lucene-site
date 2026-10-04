Title: Apache Lucene™ 10.5.2 available
category: core/news
URL:
save_as:

The Lucene PMC is pleased to announce the release of Apache Lucene 10.5.2.

Apache Lucene is a high-performance, full-featured search engine library written entirely in Java. It is a technology suitable for nearly any application that requires structured search, full-text search, faceting, nearest-neighbor search across high-dimensionality vectors, spell correction or query suggestions.

Apache Lucene 10.5.2 is a bug-fix release addressing HNSW vector search recall, Hunspell analyzer performance, and a bug in SortedNumericDocValuesRangeQuery that could yield incorrect results. Users on 10.5.1  — especially those using the aforementioned features — are encouraged to upgrade.

The release is available for immediate download at:

  <https://lucene.apache.org/core/downloads.html>

Bug fixes

* Fixed HNSW graph reconstruction that can yield worse recall (for workloads with persistent low rate of deletes) after a performance fix that was included in the 10.5.1 release. 
* Enabled Hunspell analyzer's pre-built cache activity to be interrupted
* Fixed condition that enabled analysis errors (eg from WordDelimiterFilter) to propagate and result in more serious stored field indexing failures.
* Removed the NumericFieldStats API (added in 10.5.0) and revert SortedNumericDocValuesRangeQuery to no longer use it.

Please read CHANGES.txt for a full list of changes:

  <https://lucene.apache.org/core/10_5_2/changes/Changes.html>
