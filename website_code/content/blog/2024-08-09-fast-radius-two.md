Title: Part Two: Why did Fast Radius Fail?
Date: 2024-08-09
Tags: business


> FSRD is like the holy grail of shit-SPACs.
> 
> @ItalianRicePie, Reddit 

Fast Radius went public through a SPAC on February 7, 2022 trading as FSRD on the Nasdaq. 
Just nine months later it declared bankruptcy. 
[Part one]({filename}/blog/2024-07-12-fast-radius-one.md) tried to answer, "what happened?" and part two here tries to answer "why?". 

I was there working as a data scientist and now that the ride is over I'm looking back and 
trying to figure out why the company failed.


## Finances
The tautological answer to why Fast Radius went bankrupt is because it ran out of money.
The company ran a perennial deficit because expenses exceeded revenue and once investors or banks decided to stop funding the business it failed.

| Date       | Accumulated <br/>Deficit ($M) | Revenues ($M) | Cash ($M) | Net Loss ($M) | Total Equity ($M) |
|------------|-------------------------------|---------------|-----------|---------------|-------------------|
| 12/31/2018 | $15.4                         |               |           |               |                   |
| 12/31/2019 | $33.7                         |               |           |               |                   |
| 12/31/2020 | $55.4                         | $3.5          | $5.4      |               |                   |
| 3/31/2021  | $68.4                         | $3.8          | $8.7      | $12.8         |                   |
| 6/30/2021  | $83.3                         | $4.9          | $12.3     | $14.0         | -$2.8             |
| 9/30/2021  | $100.3                        | $4.9          |           | $17.1         | -$17.1            |
| 12/31/2021 | $123.5                        | $6.4          | $8.7      | $17.0         | -$51.9            |
| 3/31/2022  | $192.9                        | $6.3          | $57.4     | $44.6         | $32.4             |
| 6/30/2022  | $215.1                        | $7.3          | $37.8     | $22.2         | $14.1             |
| 9/30/2022  | $237.3                        | $7.1          | $21.4     | $22.2         | -$5.4             |

Table 1: Quarterly finances from 10-Q SEC filings. The last three quarters represent FSRD as a publicly-traded company and the rest of the data are as reported or my estimates from yearly or six month figures. 

At the end of the first quarter of 2022, with the SPAC deal closed, Fast Radius got an infusion of $73M. 
The company had $32M in total equity and for the first time had more assets than liabilities. 
But even at its peak, assuming a historical $17M of losses per quarter the company had less than two quarters of runway.

By the September 2022 filing period Fast Radius had negative total equity and just enough cash to cover expenses for a quarter.
The last quarterly filing includes the Chapter 11 details. 

There was a last-ditch $30M stock purchase agreement from Lincoln Park that could have staved off bankruptcy.
The terms, with a minimum purchase price of $0.61 and ownership up to 20% of the company meant that the cash value was maybe $6M and not enough to make a difference.


| Date	      | Event                                                          | 	Notes                                          |
|------------|----------------------------------------------------------------|-------------------------------------------------|
| 5/1/2015   | Raised $3.8M in Seed Round 	                                   | Mitch Free and Rick Smith                       |        
| 5/3/2016	  | Raised $2.5M Seed Round	                                       | Mitch Free and Rick Smith                       |
| 3/16/2017  | Fast Radius bought and reincorporated 	                        | Lou Rassey, Pat McCusker, Bill King, John Nanry |
| 11/13/2017 | Raised $13M in Series A                                        |                                                 |
| 4/2/2019   | Raised $48M in Series B                                        |                                                 |
| 12/29/2020 | $10M SVB Loan	                                                 | Fully drawn by May 25, 2021                     |
| 5/1/2021   | $45M Palantir subscription	                                    |                                                 |
| 7/18/2021  | SPAC Merger Agreement with ENNV	                               |                                                 |
| 9/10/2021  | $20M SVB Loan	                                                 | Fully drawn by November 8, 2021                 |    
| 1/16/2022  | Fast Radius CEO Lou Rassey to be paid $2.4M cash following IPO |                                                 |
| 2/4/2022   | Closing of SPAC merger	                                        | 91% redemption rate                             |
| 2/7/2022   | IPO: NASDAQ:FSRD	                                              | Raised $73M                                     |
| 6/27/2022  | 20% layoffs                                                    |                                                 |
| 11/3/2022  | 20% layoffs                                                    |                                                 |
| 5/11/2022  | $30M purchase agreement with Lincoln Park	                     | Min price $0.25                                 |
| 11/7/2022  | Fast Radius files for Chapter 11 bankruptcy                    |                                                 |
| 12/9/2022  | SyBridge Technologies announced as winning bidder              | $15.9M                                          |

Table 2: Key events for Fast Radius. 


## CloudDDM
Fast Radius actually began in 2014 as CloudDDM (Direct Digital Manufacturing). 
Why “digital”? I don’t know – they’re printing physical plastic parts just like plastic injection molding makes parts. 

An article in 3D Print May 4, 2015, starts, “Speed is everything in this day and age, as companies try to get their products to consumers as soon as physically possible.” 
The company would locate a manufacturing facility within UPS’s hub in Louisville, KY.  
The idea was neat: you could upload an STL via the web app, configure your material and color, pay, and it’ll be printed and shipped to you. 
Next day shipping was promised as “any order placed through CloudDDM that takes under 4 hours to print and is submitted to the company by 6 pm Pacific time, will be delivered the next day”

This is a solid pitch, with a clear value proposition: get parts fast. 
However, there are a number of drawbacks if you’re interested in growing a business to make venture capital investors happy. 
One drawback is that FDM printing is slow, often taking over 4 hours to print and up to 60 hours depending on the size of the part and print settings. 
Two, there’s no benefit to scale: the way to double production is to double the printers. 
The way you scale to millions of parts is to redesign your part for plastic injection molding.

In this quick turnaround capacity there’s a limit to how big a business you can build. 
You’re printing prototypes and one-off novelties. 
The market size for additive manufacturing is $9B of the total prototype manufacturing market of $368B. 
The other problem is the 3D printing machines are relatively cheap so larger companies will purchase and run printers themselves onsite (like a super convenient microfactory!?).
After all, engineers like designing and making things.

### Fast Radius
The original Fast Radius LLC was purchased and reincorporated as Fast Radius, Inc.
by Lou Rassey, Pat McCusker, Bill King, and John Nanry in 2017 and is the company we’ll follow. 

The new management team started raising money, bringing us to April 2, 2019 [Built in Chicago](https://www.builtinchicago.org/articles/fast-radius-raises-48m) article:
> Fast Radius Raises $48M, With Plans to Double Its Team
> 
> Once the domain of hobbyists and designers, 3D printing has entered the big leagues, and investors are taking notice.
>
> Fast Radius, a Chicago-based digital manufacturing company, announced on Tuesday that it has raised a $48 million Series B round.
>
> Chief Operating Officer Pat McCusker said Fast Radius will use the funding to bolster its software development and physical engineering efforts, build new manufacturing sites and grow its sales team.
>
> “We have about 45 full-time employees, and we expect to double that in the next year or so,” said McCusker. “Most of that growth will happen in Chicago, and we’re really excited about that.”
>
> Logistics titan UPS led Tuesday’s round, in which Drive Capital also participated. Previous investors Jump Capital, Skydeck and Hyde Park Venture Partners partook in Fast Radius’ Series B as well.

A couple of notable things from here.
First, Fast Radius is positioned as Chicago-based so the UPS partnership based in Louisville, KY didn't take off. 
Second, they sell themselves as a producer of production parts (out of Chicago) rather than prototype parts for testing.
The quick turnaround concept is mentioned but the main point is that 3D printing is ready for primetime.

A new angle was mentioned here too: cloud inventory. 
You can store your part files in the cloud and print them on-demand when you need them.
It’s a nice idea but how much better is this than storing the files yourself? 

Internet Archive capture from 2019 shows an early version of the quote page. 
You fill out a form and upload a CAD file to request a quote and then sales would email or call you back. 
Simple, effective and how it worked for 20 years on the internet.

### Where did the money go?
Looking back at the financial spending, 2020 was a critical year. 
The investments made here needed to pay off. 

It was a turning point for the company too. 
The original software team delivered on the microfactory thesis and wrote software to run a 3D printing factory. 
It was an Elixir + Phoenix backend, React frontend, and all data was stored in Postgres. 
One innovation coin was spent on Elixir but otherwise Fast Radius was set to run a network of microfactories.

One by one the original software team left until it was a new team. 
The new goal was an eCommerce website like Xometry – instant quotes without needing to talk to anyone. 
This was a lot of work: analyzing the part geometry, figuring out if it could be made, figuring out how much it would cost (that was my job!) and then setting up the actual website. 

It took like a year but by 2021 that was built too! 
The problem: this “software company” didn't make much money from its software. 
Manufacturing is a traditional industry and people like relationships so most of our revenue came from big customers that didn't touch this software. 


| Date       | Employees |
|------------|-----------|
| 4/2/2019   | 45        |
| 12/31/2020 | 162       |
| 6/30/2021  | 240       |
| 12/31/2021 | 325       |

Table 3: Employee count from public news and SEC filings.


General and administrative expenses increased 396% from $7.7 million to $38.2 million for the three months ended March 31, 2022 compared to the prior-year period. 
These ballooning expenses include $17.5M in stock-based compensation (primarily to the CEO), $9.9M for Palantir (repaying their $45M loan and “using” their software).

Sidebar: what was Palantir doing? 
They were desperate to report SaaS recurring revenue that they loaned startups money which was paid back through software fees. 
Fast Radius tried and failed to shoehorn the Palantir software in somewhere. 
It didn't work out well for Palantir. 

Too many people were hired.
The baseline core 3D printing business ran with 45 people across sales, operations, and software. 
With an eCommerce business, in theory, you have a website running 24/7 that can generate revenue with zero marginal cost because serving 100 visitors costs the same as 1000. 
Manufacturing is cutting-edge but also traditional and relationship-driven so most revenue came from traditional sales processes. 
The old-school way of serving 1000 customers costs 10x more than 100 because you need to hire salespeople to serve those customers. 

Fast Radius had the worst of both worlds. 
A full software team developing software for investor demos that didn't generate sales combined with a fully staffed sales team that did generate sales. 
Neither was profitable and combined it was a money pit.  

In chasing sales, Fast Radius built a new factory on Goose Island in Chicago. 
They invested heavily in a lights-out CNC manufacturing plant for a potential sale for one customer.
It was the opposite of “do things that don’t scale” – a fully-automated factory that never ran when that big sale fell through.

There was also a new headquarters in downtown Chicago. 
Why invest in an office when the pandemic just proved remote work was effective? 
Why build manufacturing facilities in the highest cost center in the midwest? 
Because Fast Radius wanted to be seen as a software unicorn startup and not as a manufacturing company.


### The Pitch
In 2021 Fast Radius made investor presentations in the hopes of catching the SPAC wave to the public markets. 
The title slide is “Fast Radius: The First-of-its Kind Cloud Manufacturing and Digital Supply Chain Company”.
I worked there and don’t know what that means. 
Keep in mind, Fast Radius was a manufacturing company that makes money by shipping physical parts. 

It’s not clear what "Cloud Manufacturing" is but Fast Radius wasn't the first to offer contract manufacturing online.
Competitors like Xometry and Protolabs had websites where you could get quotes before Fast Radius.
The joke that the cloud is just someone else's computer applies to manufacturing too. 
With AWS, compute is so fungible that demand can be spread out across reserved and spot instances leading to high utilization. 
That’s not the case with manufacturing: parts are designed for machines which need to be programmed. 
If you want to scale up production from prototype to mid-level production you do it by moving to a machine with higher throughput – not by adding more machines. 
Nevertheless, "cloud" was the buzzword and it stuck.

The value proposition is hardly mentioned and it eschewed the traditional method of building a business described in How Venture Capital Tries and Fails To Rewrite Reality: 
> Discord grew out of the team wanting to have a convenient, feature-rich way to talk to their friends while gaming, and like almost every success story it grew slowly through making itself perfect for many, many niche communities.
> Its growth was natural, because it took all the things that you’d want from a platform and built it sustainably. 

Growing slowing out of a niche product-market fit wasn't the route Fast Radius went. 
Reading the deck you don’t get a sense of who this is for, everything is generic and broad.
The theme of the deck is buzzwords and trends.
Like how VCs tried to make Clubhouse a thing, Fast Radius tried to make Cloud Manufacturing a thing through force of will.

There’s an example customer profile with Curtiss Motorcycles but no examples of Curtiss using the Cloud Manufacturing software or platform. 
The pitch was a bunch of ideas that sounded plausibly like the "next big thing".
The problem was a lack of evidence and stories of customer adoption to make it real.

![Legacy FSRD Stock Price.png]({static}/images/Investor Presentation - Slide 5.png)
Fig 2. Fast Radius investor summary featuring a screen with my favorite line: "The biggest revolution in manufacturing since the assembly line".

Like the tautology of going bankrupt due to running out of money, could Fast Radius have been successful if the investor pitch was stronger?
Yes but it would've been a different company. 
If the company went public a year earlier at the top of the market in 2021 would it have been successful? 
Yes but the pitch would have been stronger. 

### Conclusion
Once the decision was made to take VC investment in 2019 the path was clear: growth. 
The possibility of serving a niche segment of manufacturing was foreclosed because Fast Radius needed a larger addressable market for a higher valuation.
Fast Radius took on everything to look good in a pitch to investors: 3D printing, subcontracted manufacturing from Asian suppliers, in-house manufacturing in the USA, design for manufacturing, inventory management etc. 
In the beginning, they tried to find a product-market fit, but after the funding rounds in 2020 they gave up and started throwing ideas at the wall.
The solutions were half-baked and weren't backed by paying customers. 
It takes time to build something, to build trust with customers, and that time wasn't available.
Scaling up unproven ideas wasted money.

The result was a gamble: all or nothing.
For a leadership team with stock and transaction bonuses on the line it was worth going for it.

So why did Fast Radius fail? 

1. Expenses were too high and revenue growth too low for an undifferentiated offering in a competitive space

2. The software platform didn't make money or reduce costs through operational efficiencies

3. Constantly raising money undermined the business because it couldn't find a product-market fit


### References and Links
May 4, 2015 - [CloudDDM Opens Factory at UPS's Worldwide Hub](https://3dprint.com/62642/cloudddm-ups/)

Nov 28, 2017 - [SEC Form D-Fast Radius, Inc](https://www.sec.gov/Archives/edgar/data/1723070/000172307017000001/xslFormDX01/primary_doc.xml)

April 2, 2019 [Fast Radius Raises $48M](https://www.builtinchicago.org/articles/fast-radius-raises-48m)

Jul 19, 2021 - [Investor Day Presentation | Fast Radius](https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://www.fastradius.com/wp-content/uploads/2021/07/20210719_ENNV-Fast-Radius-investor-presentation.pdf&ved=2ahUKEwiA7dPUpumHAxXbDTQIHZ9sOlIQFnoECBIQAQ&usg=AOvVaw0EQhZKsqjzslQDKLThAEWY)

Dec 6, 2021 - [How Venture Capital Tries and Fails To Rewrite Reality](https://www.wheresyoured.at/how-venture-capital-tries-and-fails/)

Mar 16, 2022 - [Fast Radius Announces Completion of Merger with ECP Environmental Growth Opportunities Corp.](https://news.thomasnet.com/companystory/fast-radius-announces-completion-of-merger-with-ecp-environmental-growth-opportunities-corp-40045944)

March 30, 2022 - [Audited Financial Report](https://www.sec.gov/ix?doc=/Archives/edgar/data/0001832351/000119312522088844/d344030d8ka.htm)

Apr 15, 2022 - https://www.reddit.com/r/SPACs/comments/u3z2it/worst_despac_of_all_time/
