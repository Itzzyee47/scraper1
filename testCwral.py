import asyncio
from crawl4ai import *
from lmuLinks import links

async def main():
    # Create a base configuration
    base_config = CrawlerRunConfig(
        word_count_threshold=200,
        wait_for="js:() => window.loaded === true"
    )

    # Create variations for different use cases
    stream_config = base_config.clone(
        stream=True,  # Enable streaming mode
        cache_mode=CacheMode.BYPASS
    )

    debug_config = base_config.clone(
        page_timeout=120000,  # Longer timeout for debugging
        verbose=True
    )
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url="http://www.landmark.cm/about-lmu",config=base_config
        )
        print(result.markdown)

if __name__ == "__main__":
    asyncio.run(main())