# Performance Budget

A performance [budget](../b/budget.md) is a quantifiable set of goals or limits that define the acceptable performance characteristics of a web application or website. In essence, it serves as a [benchmark](../b/benchmark.md) for web developers and designers to adhere to when building and deploying digital properties, ensuring that these properties deliver a smooth, efficient, and consistent user experience.

## Why Performance Budgets Matter

Performance budgets are crucial in today's digital landscape for numerous reasons:

1. **User Experience**: Slow page loads and laggy interactions frustrate users, often leading them to abandon a site or application. A performance [budget](../b/budget.md) helps prevent this by setting limits on key [performance metrics](../p/performance_metrics.md).
2. **SEO Benefits**: Search engines like Google consider page speed an important ranking [factor](../f/factor.md). Faster websites often rank higher in search results.
3. **Mobile Users**: With the increasing use of mobile devices, optimizing performance has become even more critical. Mobile users often have slower internet connections and less powerful devices.
4. **[Efficiency](../e/efficiency.md)**: Performance budgets ensure that developers focus on efficient coding practices, resulting in quicker [load](../l/load.md) times and reduced server loads.
5. **[Business](../b/business.md) Goals**: Faster sites can lead to higher conversion rates, improved user satisfaction, and greater [revenue](../r/revenue.md).

## Key Metrics for Performance Budgets

When setting a performance [budget](../b/budget.md), it is essential to focus on specific, measurable metrics. Below are some of the primary metrics used in performance budgeting:

#### 1. **Page Load Time**
   - **Definition**: The time it takes for a web page to fully [load](../l/load.md) and become interactive.
   - **Tools**: Google PageSpeed Insights, Lighthouse, WebPageTest.

#### 2. **Time to First Byte (TTFB)**
   - **Definition**: The time between a browser making an HTTP request and receiving the first byte of data from the server.
   - **Tools**: WebPageTest, Lighthouse.

#### 3. **Time to Interactive (TTI)**
   - **Definition**: The time it takes for the page to become fully interactive, meaning users can effectively interact with the page.
   - **Tools**: Lighthouse, Chrome DevTools.

#### 4. **First Contentful Paint (FCP)**
   - **Definition**: The time it takes for the browser to render the first piece of DOM content after a user navigates to your page.
   - **Tools**: Lighthouse, Chrome DevTools.

#### 5. **Speed Index**
   - **Definition**: Measures how quickly the content of a page is visually displayed during page [load](../l/load.md).
   - **Tools**: WebPageTest, Lighthouse.

#### 6. **Total Page Size**
   - **Definition**: The combined size of all assets loaded by the page, including HTML, CSS, JavaScript, images, and other resources.
   - **Tools**: Chrome DevTools, WebPageTest.

#### 7. **Number of Requests**
   - **Definition**: The total number of HTTP requests made when loading the page.
   - **Tools**: Chrome DevTools, WebPageTest.

## Implementing a Performance Budget

### Step 1: Identify Key Metrics

Determine which [performance metrics](../p/performance_metrics.md) are most crucial for your website or application. This should be based on your specific needs, target audience, and [business](../b/business.md) goals. Common metrics include [Load](../l/load.md) Time, TTFB, TTI, FCP, Speed [Index](../i/index_instrument.md), and Total Page Size.

### Step 2: Gather Baseline Data

Use performance monitoring tools like Google Lighthouse, WebPageTest, or Chrome DevTools to analyze your current website's performance. Gather data for each of the key metrics identified in the previous step.

### Step 3: Set Performance Targets

Based on the [baseline](../b/baseline.md) data, set realistic and achievable performance goals. Your targets should reflect the optimal performance levels you aim to achieve. For example, you might set a target of 3 seconds for page [load](../l/load.md) time or 1.5 seconds for TTI.

### Step 4: Incorporate Budgets Into Development Workflow

Integrate the performance [budget](../b/budget.md) into your development process. This involves:

- **Code Reviews**: Include performance criteria in code reviews to ensure new code adheres to the [budget](../b/budget.md).
- **Automated Testing**: Use tools like Lighthouse CI to run performance tests automatically whenever code is pushed to your repository.
- **Monitoring and Alerts**: Set up performance monitoring and create alerts for when performance budgets are breached.

### Step 5: Iterate and Optimize

Performance [optimization](../o/optimization.md) is an ongoing process. Regularly review performance data, refine your budgets as needed, and continue to optimize your website or application to maintain and improve performance.

## Tools for Implementing Performance Budgets

Numerous tools can assist in setting, monitoring, and enforcing performance budgets. Some of the most popular include:

- **Google Lighthouse**: An [open](../o/open.md)-source tool that audits web pages for performance, accessibility, and SEO. It provides actionable insights and can be integrated with CI/CD pipelines.
- **WebPageTest**: A tool that provides comprehensive performance data, including page [load](../l/load.md) times, TTI, FCP, and more.
- **Chrome DevTools**: A set of web developer tools built directly into the Google Chrome browser. It allows developers to inspect and improve their website’s performance.
- **Lighthouse CI**: A continuous integration tool that uses Lighthouse to audit changes in web performance automatically.

## Performance Budget Case Study: Netflix

Netflix is a prime example of a company that has successfully implemented performance budgeting to optimize its user experience. Here's a high-level overview of their approach:

### Initial Challenge

Netflix faced significant performance challenges, particularly with the initial [load](../l/load.md) time of their site and applications. They wanted to provide a seamless experience for users, regardless of their device or network speed.

### Performance Budget Implementation

1. **Identified Key Metrics**: Netflix focused on metrics such as TTI, FCP, and Total Page Size.
2. **[Baseline](../b/baseline.md) Data**: They collected [baseline](../b/baseline.md) performance data using tools like Lighthouse and internally developed monitoring systems.
3. **Target Setting**: They set aggressive performance targets to ensure a fast and responsive user experience.
4. **Integration**: Performance budgets were integrated into their development workflow. This included automated testing and code reviews focusing on performance criteria.
5. **Regular Monitoring**: Continuous performance monitoring allowed Netflix to identify and address performance regressions quickly.

### Outcomes

- **Improved [Load](../l/load.md) Times**: Netflix saw significant improvements in page [load](../l/load.md) times, reducing initial [load](../l/load.md) by several seconds.
- **Enhanced User Experience**: Users experienced more responsive and consistent interactions, leading to increased engagement and satisfaction.
- **Higher Conversion Rates**: Improved performance contributed to higher user retention rates and increased subscriptions.

For more about Netflix's approach to performance budgets, you can visit their [tech blog](https://netflixtechblog.com/).

## Conclusion

A performance [budget](../b/budget.md) is an invaluable tool for ensuring that your website or web application delivers an optimal user experience. By setting and adhering to performance targets, you can significantly improve [load](../l/load.md) times, interaction speeds, and overall [efficiency](../e/efficiency.md). The process of implementing a performance [budget](../b/budget.md) involves identifying key metrics, gathering [baseline](../b/baseline.md) data, setting realistic targets, integrating budgets into the development workflow, and continuously monitoring and optimizing performance. Using tools like Google Lighthouse, WebPageTest, and Chrome DevTools can facilitate this process, making it easier to achieve and maintain high-performance standards.