# GitHub Universe 2026: full session catalog

Every session in the Universe 2026 catalog (161 time slots, Oct 26-29), with a ready-to-paste JSON block for the schedule app. Sessions that run more than once are listed at each time.

## How to add a session to your badge

1. Find the session below and copy its JSON block.
2. Paste it into the `"sessions": [ ... ]` list in `apps/schedule/schedule.json`. Put a comma between sessions, but not after the last one.
3. Make sure your `"rooms"` map has the session's room. The [rooms block](#rooms) below has every catalog location (the same list as `schedule.json.sample`), so you can paste it over your `"rooms"` map.
4. Check your file on a computer: `python3 tools/validate_schedule.py`.

Each `note` is a shortened description. Change it to whatever helps you on the day, such as why you're going or a question to ask.

**Jump to a day:** [Monday, Oct 26](#monday-oct-26) · [Tuesday, Oct 27](#tuesday-oct-27) · [Wednesday, Oct 28](#wednesday-oct-28) · [Thursday, Oct 29](#thursday-oct-29)

## Rooms

Replace the whole `"rooms": { ... }` entry in your `schedule.json` with this, keeping the comma that follows it:

```json
"rooms": {
  "Hotel Zephyr": {"building": "250 Beach St"},
  "Main Stage": {"building": "Festival Pavilion"},
  "Silent Disco Breakouts": {"building": "Festival Pavilion"},
  "Demos & Donuts (Level 2)": {"building": "Gateway Pavilion"},
  "Cowell Theater": {"building": "Gateway Pavilion"},
  "Ship & Tell": {"building": "Firehouse"},
  "Sandbox, 3rd Floor": {"building": "Building C"},
  "Silent Disco Demos": {"building": "Festival Pavilion"},
  "The Speakeasy (GitHub Central)": {"building": "Festival Pavilion"},
  "Workshops (Level 1)": {"building": "Gateway Pavilion"},
  "Outdoor Theater": {"building": "Gateway Plaza"},
  "The Interval": {"building": "Building A"},
  "BATS Theatre, 3rd Floor": {"building": "Building B"},
  "Equator Coffee": {"building": "Fort Mason"},
  "Radhaus": {"building": "Fort Mason"},
  "Bar Darling": {"building": "2263 Chestnut St"},
  "Barebottle Beer Garden": {"building": "1525 Cortland Ave"},
  "Barrio": {"building": "900 North Point St"},
  "Broad Street Oyster Co": {"building": "900 North Point St"},
  "Culinary Artistas": {"building": "851 Beach St"},
  "Figma HQ": {"building": "760 Market St"},
  "Flores San Francisco": {"building": "2030 Union St"},
  "For the Record": {"building": "2120 Greenwich St"},
  "Left Door": {"building": "1905 Union St"},
  "Pier 43 1/2": {"building": "Fisherman's Wharf"},
  "Redwood Empire Whiskey": {"building": "Redwood Empire Whiskey"},
  "San Francisco Brewing Co.": {"building": "3150 Polk St"},
  "Subpar Miniature Golf": {"building": "900 North Point St"},
  "The Civic Kitchen": {"building": "2961 Mission St"},
  "Tonga Room & Hurricane Bar": {"building": "Fairmont Hotel"}
}
```

## Monday, Oct 26

### 6:30 PM

#### A Taste of the Craft - Hosted by Rewind

**Monday, Oct 26 · 6:30 PM - 9:00 PM PDT**  
**Where:** Redwood Empire Whiskey  
**Type:** Social

Step behind the scenes at Redwood Empire Whiskey for an intimate evening of whiskey, craftsmanship, and indulgence, hosted by Master Blender Lauren Patz. Begin with a private tour of the facility before settling in for a 60-minute blending seminar, where you’ll explore the art of whiskey-making and create your own blend under the guidance of a true expert. Then, take it outside to the Waterfront Terrace for an elevated dinner overlooking the water, paired with one drink per guest.

Hosted by Rewind. Advanced registration coming soon.

```json
{"day": "2026-10-26", "start": "18:30", "end": "21:00",
 "title": "A Taste of the Craft - Hosted by Rewind", "room": "Redwood Empire Whiskey",
 "speaker": "",
 "note": "Step behind the scenes at Redwood Empire Whiskey for an intimate evening of whiskey, craftsmanship, and indulgence, hosted by Master..."}
```

## Tuesday, Oct 27

### 3:00 PM

#### Universe Badge Pickup Party!

**Tuesday, Oct 27 · 3:00 PM - 7:00 PM PDT**  
**Where:** Hotel Zephyr @ 250 Beach St  
**Type:** Special Event

Skip the line, stack the nachos. Come pick up your badge early at Hotel Zephyr where you can grab a snack and a drink, meet your people and score exclusive Universe merch you can't get anywhere else.

```json
{"day": "2026-10-27", "start": "15:00", "end": "19:00",
 "title": "Universe Badge Pickup Party!", "room": "Hotel Zephyr",
 "speaker": "",
 "note": "Skip the line, stack the nachos. Come pick up your badge early at Hotel Zephyr where you can grab a snack and a drink, meet your people..."}
```

### 5:00 PM

#### San Francisco Syntax Meetup

**Tuesday, Oct 27 · 5:00 PM - 7:00 PM PDT**  
**Where:** Barebottle Beer Garden @ 1525 Cortland Ave  
**Type:** Social

We're in town for GitHub Universe! Come hang out with the whole Syntax crew at Barebottle Beer Garden at Salesforce Park The last two years' events were so great that we're running it back AGAIN!! Join us for a SF Syntax Meetup, a laid-back event for all web developers and coding lovers! This in-person event will take place at Barebottle Beer Garden at Salesforce Park in San Francisco the day before GitHub Universe. No agenda, come hang out, talk to Scott, Wes, CJ, the rest of the Syntax crew and some folks from Sentry, and have a good time!

Hosted by Syntax. Advance registration required .

```json
{"day": "2026-10-27", "start": "17:00", "end": "19:00",
 "title": "San Francisco Syntax Meetup", "room": "Barebottle Beer Garden",
 "speaker": "",
 "note": "Join us for a SF Syntax Meetup, a laid-back event for all web developers and coding lovers!"}
```

## Wednesday, Oct 28

### 9:00 AM

#### Opening Keynote

**Wednesday, Oct 28 · 9:00 AM - 9:45 AM PDT**  
**Where:** Main Stage @ Festival Pavilion  
**Type:** Keynote · **Format:** In-person, Recorded, Livestream, AI summary

Join us for the opening keynote as we look at the next era of software, the developers building it, and the tools and workflows GitHub is creating to help them go further. Expect new announcements, live demos, and a few surprises along the way.

**Speakers**

- Jay Parikh: Executive Vice President, CoreAI, Microsoft
- April Leonard: VP, Engineering, GitHub
- Cassidy Williams: Sr. Director, Developer Advocacy, GitHub
- Damian Brady: Staff Developer Advocate, GitHub
- Burke Holland: Principal Cloud Advocate, Microsoft

```json
{"day": "2026-10-28", "start": "09:00", "end": "09:45",
 "title": "Opening Keynote", "room": "Main Stage",
 "speaker": "Jay Parikh (Microsoft), April Leonard (GitHub), Cassidy Williams (GitHub), Damian Brady (GitHub), Burke Holland (Microsoft)",
 "note": "Join us for the opening keynote as we look at the next era of software, the developers building it, and the tools and workflows GitHub..."}
```

#### Watch the Keynote from Cowell Theater

**Wednesday, Oct 28 · 9:00 AM - 9:45 AM PDT**  
**Where:** Cowell Theater @ Gateway Pavilion  
**Type:** Special Event

The full keynote streams live in Cowell Theater. If you’d like a quieter place to take it in or just want a comfortable seat with a great view of the screen, this is your spot. Same keynote, same start time, your choice of setting.

```json
{"day": "2026-10-28", "start": "09:00", "end": "09:45",
 "title": "Watch the Keynote from Cowell Theater", "room": "Cowell Theater",
 "speaker": "",
 "note": "The full keynote streams live in Cowell Theater. If you'd like a quieter place to take it in or just want a comfortable seat with a..."}
```

#### Watch the Keynote from the Outdoor Theater

**Wednesday, Oct 28 · 9:00 AM - 9:45 AM PDT**  
**Where:** Outdoor Theater @ Gateway Plaza  
**Type:** Special Event · **Format:** In-person

The full keynote streams live here under the tent. Whether you want a bit of fresh air or a more relaxed way to take it all in, grab a spot and settle in. Same keynote, same start time, your choice of setting.

```json
{"day": "2026-10-28", "start": "09:00", "end": "09:45",
 "title": "Watch the Keynote from the Outdoor Theater", "room": "Outdoor Theater",
 "speaker": "",
 "note": "The full keynote streams live here under the tent. Whether you want a bit of fresh air or a more relaxed way to take it all in, grab a..."}
```

### 10:15 AM

#### Agentic Workflows: Automation at scale

**Wednesday, Oct 28 · 10:15 AM - 10:45 AM PDT**  
**Where:** The Speakeasy @ GitHub Central, Festival Pavilion  
**Type:** Breakout Session · **Format:** In-person, AI summary

Automation is how we buy time for craft, enforce correctness in situations that require judgment, and improve our software at business scale. Learn how to start automating, as well as how you can start to setup your software factory with governance, monitoring, and security so you can roll out automations to everyone in your business!

**Speakers**

- Landon Cox: Senior Principle Researcher, Microsoft
- Peli de Halleux: Agentic Engineer, GitHub Next, Microsoft

```json
{"day": "2026-10-28", "start": "10:15", "end": "10:45",
 "title": "Agentic Workflows: Automation at scale", "room": "The Speakeasy (GitHub Central)",
 "speaker": "Landon Cox (Microsoft), Peli de Halleux (Microsoft)",
 "note": "Learn how to start automating, as well as how you can start to setup your software factory with governance, monitoring, and security so..."}
```

### 10:30 AM

#### Shut the context window! You're letting the tokens out

**Wednesday, Oct 28 · 10:30 AM - 10:45 AM PDT**  
**Where:** Demos & Donuts @ Gateway Pavilion, Level 2  
**Type:** Product Demo · **Format:** In-person, AI summary

GitHub Copilot builds context from your open files, related code, and conversation history before every interaction, but most developers never see how much that payload grows. Understanding that mechanism is the difference between sharp output and token bloat. 

In this session, Dylan McCarthy shows how Copilot constructs context in practice, demonstrates the developer habits that quietly inflate token usage, and walks through focused workflows that produce better results with less overhead. 

Dylan will also demo lightweight GitHub-native guardrails that help teams catch overly broad changes before they merge. You'll leave with a mental model of context mechanics and practical patterns you can apply immediately.

**Speakers**

- Dylan McCarthy: Principal Consultant, Nexwave

```json
{"day": "2026-10-28", "start": "10:30", "end": "10:45",
 "title": "Shut the context window! You're letting the tokens out", "room": "Demos & Donuts (Level 2)",
 "speaker": "Dylan McCarthy (Nexwave)",
 "note": "Dylan McCarthy shows how Copilot constructs context in practice, demonstrates the developer habits that quietly inflate token usage, and..."}
```

#### Agentic engineering past the pilot: An enterprise playbook

**Wednesday, Oct 28 · 10:30 AM - 11:10 AM PDT**  
**Where:** Cowell Theater @ Gateway Pavilion  
**Type:** Breakout Session · **Format:** In-person, AI summary

The industry has moved from code completion to chat to agents, and now into AI-native software delivery. But what does that actually look like inside an enterprise, where governance, developer experience, and adoption at scale all have to coexist? 

Through live demos spanning IDE, CLI, and multi-session orchestration, Nick Liffen and Philip Holleran will share the system-level patterns that move agentic engineering from experiment to operating model.

**Speakers**

- Nick Liffen: VP, GTM Strategy, GitHub
- Philip Holleran: Field CTO, GitHub

```json
{"day": "2026-10-28", "start": "10:30", "end": "11:10",
 "title": "Agentic engineering past the pilot: An enterprise playbook", "room": "Cowell Theater",
 "speaker": "Nick Liffen (GitHub), Philip Holleran (GitHub)",
 "note": "The industry has moved from code completion to chat to agents, and now into AI-native software delivery."}
```

#### How one open source project turned funding into security at scale

**Wednesday, Oct 28 · 10:30 AM - 11:10 AM PDT**  
**Where:** BATS Theatre @ Fort Mason Building B, 3rd Floor  
**Type:** Breakout Session · **Format:** In-person, AI summary

As AI agents write more code, open source maintainers face a defining challenge: how do you scale security as fast as software creation? This session pairs the GitHub Secure Open Source Fund with ScanAPI's one-year journey from funding to measurable security outcomes. Camila Maia and Gregg Cochran show how AI security education, tools, and GitHub Copilot helped one project build safer practices, then scale them across three organizations, 200+ contributors, and Portuguese-speaking communities. Leave with a practical blueprint for turning funding, AI, and community into community-powered security impact.

**Speakers**

- Gregg Cochran: Staff Program Manager, GitHub
- Camila Maia: Co-founder, Cumbuca Dev

```json
{"day": "2026-10-28", "start": "10:30", "end": "11:10",
 "title": "How one open source project turned funding into security at scale", "room": "BATS Theatre, 3rd Floor",
 "speaker": "Gregg Cochran (GitHub), Camila Maia (Cumbuca Dev)",
 "note": "This session pairs the GitHub Secure Open Source Fund with ScanAPI's one-year journey from funding to measurable security outcomes."}
```

#### Your benchmark is lying: What evals actually look like

**Wednesday, Oct 28 · 10:30 AM - 11:15 AM PDT**  
**Where:** Sandbox @ Fort Mason Building C, Founders Inc., 3rd Floor  
**Type:** Sandbox Session · **Format:** In-person

Public benchmarks suggest AI coding tools are nearly solved. Developer feedback tells a different story. After a year of shipping models from multiple frontier labs inside GitHub Copilot, the team has learned that the gap between "scores well on SWE-bench" and "developers actually keep using it" is enormous and widening. 

Julia Kasper and Walker Chabbott go behind the scenes on how GitHub Copilot evaluates models in production: what they measure, what they've stopped measuring, the signals that correlate with real developer outcomes, and why your favorite leaderboard may be leading your team astray. You'll leave with a practical framework for building your own eval system (no dedicated research team required).

**Speakers**

- Walker Chabbott: Product Manager III, GitHub
- Julia Kasper: Product Manager, Microsoft

```json
{"day": "2026-10-28", "start": "10:30", "end": "11:15",
 "title": "Your benchmark is lying: What evals actually look like", "room": "Sandbox, 3rd Floor",
 "speaker": "Walker Chabbott (GitHub), Julia Kasper (Microsoft)",
 "note": "You'll leave with a practical framework for building your own eval system (no dedicated research team required)."}
```

#### Securing MCP: Real exploits, what actually mitigates them, and what doesn't

**Wednesday, Oct 28 · 10:30 AM - 12:00 PM PDT**  
**Where:** Workshops @ Gateway Pavilion, Level 1  
**Type:** Workshop · **Format:** In-person

There's a running joke that the "S" in MCP stands for security. Funny, but is it fair? MCP is showing up in production and in sensitive environments faster than its security story is settling, and it's worth asking what you're actually exposed to.

This interactive session breaks down MCP security as it really stands today: what the threats are, which layer each one operates on, and how to host MCP servers in production without opening yourself up. You'll look at real exploits and vulnerabilities that have already surfaced, sort the mitigations that hold up from the ones that don't, and dig into where the spec and ecosystem still leave gaps, drawing on what GitHub has learned running this in the real world.

You'll leave with a clear view of MCP's current risks and a practical sense of what's safe to do today, what isn't yet, and what to watch as the ecosystem matures.

**Speakers**

- Sam Morrow: Staff Software Engineer, GitHub

```json
{"day": "2026-10-28", "start": "10:30", "end": "12:00",
 "title": "Securing MCP: Real exploits, what actually mitigates them, and what doesn't", "room": "Workshops (Level 1)",
 "speaker": "Sam Morrow (GitHub)",
 "note": "You'll leave with a clear view of MCP's current risks and a practical sense of what's safe to do today, what isn't yet, and what to..."}
```

### 10:50 AM

#### Modernizing CI/CD with agents, GitHub Actions, and human oversight
 (Sponsored)

**Wednesday, Oct 28 · 10:50 AM - 11:05 AM PDT**  
**Where:** Demos & Donuts @ Gateway Pavilion, Level 2  
**Type:** Product Demo · **Format:** In-person, AI summary

At enterprise scale, CI/CD modernization can feel less like a migration and more like untangling years of custom pipelines, dependencies, controls, and delivery commitments. This session will demonstrate how agents helped CVS Health and UST moved from Jenkins to GitHub Actions by reducing repetitive work and keeping engineers in full control. 

You’ll see how an enterprise put agents to work in a complex migration, and leave with a practical way to plan a CI/CD modernization that addresses legacy complexity today while creating a foundation for future agent-powered development.

**Speakers**

- Mitch Enderle: Executive Director, Platform Engineering, CVS Health
- Sai Gade: Global Head - AIDLC, Platform Engineering & SRE, UST

```json
{"day": "2026-10-28", "start": "10:50", "end": "11:05",
 "title": "Modernizing CI/CD with agents, GitHub Actions, and human oversight (Sponsored)", "room": "Demos & Donuts (Level 2)",
 "speaker": "Mitch Enderle (CVS Health), Sai Gade (UST)",
 "note": "This session will demonstrate how agents helped CVS Health and UST moved from Jenkins to GitHub Actions by reducing repetitive work and..."}
```

### 11:00 AM

#### Inside the Lab with GitHub Next

**Wednesday, Oct 28 · 11:00 AM - 11:30 AM PDT**  
**Where:** The Speakeasy @ GitHub Central, Festival Pavilion  
**Type:** Breakout Session · **Format:** In-person, AI summary

Next is constantly exploring the future shape of software development. Come by for demos of our research projects, and discussions about the themes that we believe are durably important to how we all create software.

**Speakers**

- Alex Gorischek: Senior Research Engineer, GitHub
- Maggie Appleton: Staff Research Engineer, GitHub
- David Slater: Director, Research, GitHub
- Idan Gazit: Head of GitHub Next, GitHub

```json
{"day": "2026-10-28", "start": "11:00", "end": "11:30",
 "title": "Inside the Lab with GitHub Next", "room": "The Speakeasy (GitHub Central)",
 "speaker": "Alex Gorischek (GitHub), Maggie Appleton (GitHub), David Slater (GitHub), Idan Gazit (GitHub)",
 "note": "Next is constantly exploring the future shape of software development."}
```

### 11:10 AM

#### Stop malicious packages before they reach your build with GitHub Package Firewall

**Wednesday, Oct 28 · 11:10 AM - 11:25 AM PDT**  
**Where:** Demos & Donuts @ Gateway Pavilion, Level 2  
**Type:** Product Demo · **Format:** In-person, AI summary

A wave of recent high-profile attacks has exploited a single weakness: the privileges baked into CI/CD pipelines. An attacker who lands a malicious package in your build can steal the credentials your runner holds, or inject malware that ships to everyone downstream. Securing the build environment has never mattered more.

GitHub Package Firewall sits between your build and upstream package registries, screening dependencies before they ever reach your runner, so a compromised package is blocked at the door instead of executing with your pipeline's privileges. It's a new service and free to use.

In this session, you'll see how the firewall works, how to put it in front of your own builds, and how it protects the users who depend on what you ship.

**Speakers**

- Eric Sorenson: Senior Product Manager, GitHub

```json
{"day": "2026-10-28", "start": "11:10", "end": "11:25",
 "title": "Stop malicious packages before they reach your build with GitHub Package Firewall", "room": "Demos & Donuts (Level 2)",
 "speaker": "Eric Sorenson (GitHub)",
 "note": "You'll see how the firewall works, how to put it in front of your own builds, and how it protects the users who depend on what you ship."}
```

### 11:15 AM

#### Humans set direction. Agents close the loop.

**Wednesday, Oct 28 · 11:15 AM - 11:45 AM PDT**  
**Where:** Main Stage @ Festival Pavilion  
**Type:** Main Stage · **Format:** In-person, Recorded, AI summary

The value of an agent isn’t measured by how much code it writes, but by how much software work it finishes. Agents are moving beyond code generation to help plan, review, secure, deploy, and operate software. In this session, GitHub Chief Product Officer Mario Rodriguez explores a new operating model where developers define the outcomes and standards, agents carry work through the development loop, and people remain accountable for what ships. See how GitHub is connecting the context, workflows, and controls teams need to delegate more ambitious work with confidence.

**Speakers**

- Mario Rodriguez: Chief Product Officer, GitHub
- Evan Boyle: Partner Director of Engineering, GitHub

```json
{"day": "2026-10-28", "start": "11:15", "end": "11:45",
 "title": "Humans set direction. Agents close the loop.", "room": "Main Stage",
 "speaker": "Mario Rodriguez (GitHub), Evan Boyle (GitHub)",
 "note": "GitHub Chief Product Officer Mario Rodriguez explores a new operating model where developers define the outcomes and standards, agents..."}
```

### 11:20 AM

#### I made my Octolamp think with GitHub Copilot CLI hooks

**Wednesday, Oct 28 · 11:20 AM - 11:35 AM PDT**  
**Where:** Ship & Tell @ Firehouse  
**Type:** Ship & Tell · **Format:** In-person, Recorded, AI summary

At Universe 2025, GitHub handed out Octolamps. Beatris Mendez Gandica wondered: what if hers could show when GitHub Copilot CLI is thinking? So she built it.

Using the native hooks system, her lamp breathes green when the agent works, goes white when idle, and blinks red on errors. No prompting tricks, just system-level lifecycle events driving a physical light via the WLED API. 

In this session, Beatris shows what she built, how Copilot CLI hooks work under the hood, and why connecting software to hardware made the concept click. You'll leave knowing how to write your own hooks for any use case. (Pro tip: the repo is open source and works with any WLED device!)

**Speakers**

- Bea Mendez Gandica: CEO/Founder, Nuevo Foundation

```json
{"day": "2026-10-28", "start": "11:20", "end": "11:35",
 "title": "I made my Octolamp think with GitHub Copilot CLI hooks", "room": "Ship & Tell",
 "speaker": "Bea Mendez Gandica (Nuevo Foundation)",
 "note": "Beatris shows what she built, how Copilot CLI hooks work under the hood, and why connecting software to hardware made the concept click."}
```

### 11:30 AM

#### Four primitives to evaluate and improve your on-call agent's autonomy (Sponsored)

**Wednesday, Oct 28 · 11:30 AM - 11:45 AM PDT**  
**Where:** Demos & Donuts @ Gateway Pavilion, Level 2  
**Type:** Product Demo · **Format:** In-person, AI summary

On-call isn't a single kind of work, so treating agent autonomy as one switch (trusted or not) breaks down fast. This session splits on-call into four primitives: triaging alerts, investigating them, acting on production, and learning from what happened. Each progresses at a different rate: investigation is bottlenecked on quality, while action is limited by trust. We'll share how we build frontier agents at Resolve AI, including the shadow diff we use to tell which limit you're actually against, and how to promote and demote autonomy safely, per decision class rather than per agent. You'll leave able to place your own on-call agents against a working reference and know where to focus to improve them.

**Speakers**

- Steven Karis: Chief Architect, ResolveAI

```json
{"day": "2026-10-28", "start": "11:30", "end": "11:45",
 "title": "Four primitives to evaluate and improve your on-call agent's autonomy (Sponsored)", "room": "Demos & Donuts (Level 2)",
 "speaker": "Steven Karis (ResolveAI)",
 "note": "This session splits on-call into four primitives: triaging alerts, investigating them, acting on production, and learning from what..."}
```

#### Supercharge Copilot code review with custom review instructions

**Wednesday, Oct 28 · 11:30 AM - 11:45 AM PDT**  
**Where:** Silent Disco Demos @ Festival Pavilion  
**Type:** Product Demo · **Format:** In-person, Recorded, AI summary

GitHub's Dependabot team added custom Copilot code review instructions to their 10-year-old backend repository, and the results showed up fast: review time dropped, comment volume dropped, and Copilot now automatically catches real, domain-specific bugs that used to require a human reviewer to spot.

The key was where the instructions came from. Instead of writing review rules from scratch, the team used Copilot to mine their own PR review history for the patterns their reviewers flag again and again, then turned those recurring patterns into custom instruction files. The result is a reviewer that already knows the conventions, pitfalls, and domain quirks of a decade-old codebase.

This session walks through exactly how they did it, and how you can run the same workflow on your own repository.

**Speakers**

- Nish Sinha: Software Engineer III, GitHub

```json
{"day": "2026-10-28", "start": "11:30", "end": "11:45",
 "title": "Supercharge Copilot code review with custom review instructions", "room": "Silent Disco Demos",
 "speaker": "Nish Sinha (GitHub)",
 "note": "This session walks through exactly how they did it, and how you can run the same workflow on your own repository."}
```

#### Building AI fluency at UPS

**Wednesday, Oct 28 · 11:30 AM - 12:10 PM PDT**  
**Where:** Cowell Theater @ Gateway Pavilion  
**Type:** Breakout Session · **Format:** In-person, AI summary

Getting developers to try GitHub Copilot is simple. Getting them fluent with it — using agents to plan, write, and ship real work — is the harder challenge. This session shares how UPS is tackling that, from a developer-focused architect's perspective: how developers move from awareness to fluency, why motivation and measurement matter as much as the tooling, and how faster code generation shifts bottlenecks to new places across the SDLC.

You'll leave with a practical view of what building AI fluency actually takes at enterprise scale, and where to focus first.

**Speakers**

- Jared Hatfield: Principal Application Architect, UPS

```json
{"day": "2026-10-28", "start": "11:30", "end": "12:10",
 "title": "Building AI fluency at UPS", "room": "Cowell Theater",
 "speaker": "Jared Hatfield (UPS)",
 "note": "This session shares how UPS is tackling that, from a developer-focused architect's perspective: how developers move from awareness to..."}
```

#### How GitHub taught Copilot to remember and when to forget

**Wednesday, Oct 28 · 11:30 AM - 12:10 PM PDT**  
**Where:** BATS Theatre @ Fort Mason Building B, 3rd Floor  
**Type:** Breakout Session · **Format:** In-person, AI summary

Real developer work is sequential, but today's AI agents treat every task as a fresh start. What if Copilot could carry forward what it learned from your last session and drop what no longer applies? 

Alejandro Carderera De Diego and Cooper Nederhood built a benchmark from chains of real GitHub pull requests to test this and found a counterintuitive result: accumulated context can hurt performance. 

That finding powered two features now in development: Skill Forge and Copilot REM. In this session, you'll learn how both work, the measurable improvements they produce, and how to apply these principles to your own agent workflows.

**Speakers**

- Cooper Nederhood: Senior Applied Researcher, GitHub
- Alejandro Carderera: Staff Applied Researcher, GitHub

```json
{"day": "2026-10-28", "start": "11:30", "end": "12:10",
 "title": "How GitHub taught Copilot to remember and when to forget", "room": "BATS Theatre, 3rd Floor",
 "speaker": "Cooper Nederhood (GitHub), Alejandro Carderera (GitHub)",
 "note": "You'll learn how both work, the measurable improvements they produce, and how to apply these principles to your own agent workflows."}
```

### 11:40 AM

#### Real ways we cut token costs without slowing developers

**Wednesday, Oct 28 · 11:40 AM - 12:25 PM PDT**  
**Where:** Sandbox @ Fort Mason Building C, Founders Inc., 3rd Floor  
**Type:** Sandbox Session · **Format:** In-person

AI coding tools can boost productivity, but they can also increase costs. Token-based pricing changes how teams think about performance, efficiency, and even code quality. But many don’t see where tokens are being wasted until it hurts. 

This session will show you real examples of token waste — bloated prompts, repeated context, noisy CI workflows — along with practical changes you can implement to reduce consumption without slowing down developers. You’ll also learn how to identify common sources of waste, optimize token usage, and scale AI-assisted development more efficiently.

**Speakers**

- Heejin Lee: Senior Solutions Engineer, GitHub

```json
{"day": "2026-10-28", "start": "11:40", "end": "12:25",
 "title": "Real ways we cut token costs without slowing developers", "room": "Sandbox, 3rd Floor",
 "speaker": "Heejin Lee (GitHub)",
 "note": "This session will show you real examples of token waste - bloated prompts, repeated context, noisy CI workflows - along with practical..."}
```

### 11:50 AM

#### Four days, zero lines: The AI force multiplier

**Wednesday, Oct 28 · 11:50 AM - 12:05 PM PDT**  
**Where:** Ship & Tell @ Firehouse  
**Type:** Ship & Tell · **Format:** In-person, Recorded, AI summary

How do you clear a massive governance backlog without destroying developer velocity? In just four days, Jeff Doolittle of Trimble used GitHub Copilot to build an automated system and rapidly clear the backlog without manually writing a single line of code. In this session, you’ll learn how to use AI not just as a coding assistant, but as an architectural force multiplier. 

You'll leave knowing how to combine automated GitHub Actions with custom Copilot prompts. This combination will give you the tools to eliminate developer toil, easily enforce remediation lifecycles, empower others to adopt AI tools, and make the "right path" the easiest path for your entire engineering org.

**Speakers**

- Jeff Doolittle: Distinguished Engineer, Principal Architect, Trimble

```json
{"day": "2026-10-28", "start": "11:50", "end": "12:05",
 "title": "Four days, zero lines: The AI force multiplier", "room": "Ship & Tell",
 "speaker": "Jeff Doolittle (Trimble)",
 "note": "You'll learn how to use AI not just as a coding assistant, but as an architectural force multiplier."}
```

#### GitHub Copilot and Windows: Bringing local models into the workflow

**Wednesday, Oct 28 · 11:50 AM - 12:05 PM PDT**  
**Where:** Silent Disco Demos @ Festival Pavilion  
**Type:** Product Demo · **Format:** In-person, Recorded, AI summary

How should developers use local and cloud intelligence together? GitHub and Windows show how Copilot's intelligent orchestration can bring local models into the Copilot workflow. GitHub provides the developer experience and orchestration; Windows provides the hardware, runtime, and optimized environment for on-device inference. This session will explore how Auto mode can help match work to the right compute environment while keeping local and cloud intelligence complementary.

**Speakers**

- Ryan Hecht: Product Manager, GitHub

```json
{"day": "2026-10-28", "start": "11:50", "end": "12:05",
 "title": "GitHub Copilot and Windows: Bringing local models into the workflow", "room": "Silent Disco Demos",
 "speaker": "Ryan Hecht (GitHub)",
 "note": "This session will explore how Auto mode can help match work to the right compute environment while keeping local and cloud intelligence..."}
```

#### Supply chain controls for AI agents with JFrog and GitHub (Sponsored)

**Wednesday, Oct 28 · 11:50 AM - 12:05 PM PDT**  
**Where:** Demos & Donuts @ Gateway Pavilion, Level 2  
**Type:** Product Demo · **Format:** In-person, AI summary

As AI agents produce more code, teams need to know what those agents bring into a build and how to verify what ships. This demo shows how JFrog works with GitHub to control which models, MCP servers, and packages agents use; replace supported vulnerable dependencies with patched versions when available; and enforce compliance policies using signed evidence. You’ll see where those controls fit in the development workflow and what teams can review when auditing a release.

**Speakers**

- Ronen Lewit: VP Strategics and Field CTO, JFrog

```json
{"day": "2026-10-28", "start": "11:50", "end": "12:05",
 "title": "Supply chain controls for AI agents with JFrog and GitHub (Sponsored)", "room": "Demos & Donuts (Level 2)",
 "speaker": "Ronen Lewit (JFrog)",
 "note": "This demo shows how JFrog works with GitHub to control which models, MCP servers, and packages agents use; replace supported vulnerable..."}
```

### 12:00 PM

#### Session After Party: Humans set direction. Agents close the loop.

**Wednesday, Oct 28 · 12:00 PM - 12:30 PM PDT**  
**Where:** The Speakeasy @ GitHub Central, Festival Pavilion  
**Type:** Session After Party · **Format:** In-person

This is an informal follow-up Q&A to the main stage session "Humans set direction. Agents close the loop." Right after the presentation, join us for the discussion in GitHub Central. Bring your questions and keep the conversation going.

**Speakers**

- Mario Rodriguez: Chief Product Officer, GitHub
- Evan Boyle: Partner Director of Engineering, GitHub

```json
{"day": "2026-10-28", "start": "12:00", "end": "12:30",
 "title": "Session After Party: Humans set direction. Agents close the loop.", "room": "The Speakeasy (GitHub Central)",
 "speaker": "Mario Rodriguez (GitHub), Evan Boyle (GitHub)",
 "note": "This is an informal follow-up Q&A to the main stage session \"Humans set direction."}
```

### 12:10 PM

#### Beyond correct: Making code quality worth acting on

**Wednesday, Oct 28 · 12:10 PM - 12:25 PM PDT**  
**Where:** Demos & Donuts @ Gateway Pavilion, Level 2  
**Type:** Product Demo · **Format:** In-person, AI summary

When AI generates more code, static analysis surfaces more findings. More findings should mean better code. Instead, it usually means more noise nobody acts on.

Over the past year, the team measured that problem across 165,000+ pull requests and 100K+ repositories. The data was pointed: 54% of PRs with findings have the same rule firing over and over, and developers dismiss quality findings at nearly the same rate as security findings while perceiving them as far noisier.

This session turns that research into practical guidance: why "more findings" backfires, the design philosophy that finally moved adoption, and specific decisions traced back to the data, like grouping repeated findings into one comment and surfacing fixes inline instead of in a dashboard nobody opened. Expect live demos and real before-and-after PR examples. You'll leave knowing how to make automated feedback something developers actually trust and act on.

**Speakers**

- Caro Galvin: Senior Product Manager, GitHub

```json
{"day": "2026-10-28", "start": "12:10", "end": "12:25",
 "title": "Beyond correct: Making code quality worth acting on", "room": "Demos & Donuts (Level 2)",
 "speaker": "Caro Galvin (GitHub)",
 "note": "This session turns that research into practical guidance: why \"more findings\" backfires, the design philosophy that finally moved..."}
```

### 12:20 PM

#### The Low Orbit Agentic Cannon: Scaling Copilot through internal tooling

**Wednesday, Oct 28 · 12:20 PM - 12:35 PM PDT**  
**Where:** Ship & Tell @ Firehouse  
**Type:** Ship & Tell · **Format:** In-person, Recorded, AI summary

In December 2025, more than 300 autonomous pull requests were opened in a single morning — each written by an AI agent. By March 2026, the same approach generated more than 3,500 architecture documentation files across the organization. This resulted in a 97% success rate, driven by one engineer. 

This session shares how the Galaxy team internally developed the tools behind this effort: from Air Traffic Controller, which routed Jira tickets to Copilot cloud agents, to the Low Orbit Agentic Cannon, which scaled work across hundreds of repositories. 

You'll learn what worked, what stalled, and the lessons gained from operating agentic systems at scale, along with why proven engineering fundamentals mattered more than the AI itself.

**Speakers**

- Callum Cieciala: VP, Developer Experience, Galaxy

```json
{"day": "2026-10-28", "start": "12:20", "end": "12:35",
 "title": "The Low Orbit Agentic Cannon: Scaling Copilot through internal tooling", "room": "Ship & Tell",
 "speaker": "Callum Cieciala (Galaxy)",
 "note": "This session shares how the Galaxy team internally developed the tools behind this effort: from Air Traffic Controller, which routed..."}
```

### 12:30 PM

#### Build once, run on any agent: a practical guide to agent skills

**Wednesday, Oct 28 · 12:30 PM - 1:10 PM PDT**  
**Where:** Cowell Theater @ Gateway Pavilion  
**Type:** Breakout Session · **Format:** In-person, AI summary

Most developers use AI the same way: open a chat, type a prompt, move on. The context disappears. The next step starts from scratch. Skills break that cycle: reusable files that capture how you want an agent to work. Andrea Griffiths builds them for her own recurring work: files any coding agent can run. Shishir Tewari builds them for a data engineering team at Procore, where a skill has to encode senior-engineer judgment and survive production. Different scale, same format. The file you write for yourself tonight is the same file that runs a team's pipeline.

After this session, you'll have a clear model for when to build a skill instead of writing another prompt.

**Speakers**

- Andrea Griffiths: Senior Developer Advocate, GitHub
- Shishir Tewari: Senior Manager, Data Engineering, Procore Technologies

```json
{"day": "2026-10-28", "start": "12:30", "end": "13:10",
 "title": "Build once, run on any agent: a practical guide to agent skills", "room": "Cowell Theater",
 "speaker": "Andrea Griffiths (GitHub), Shishir Tewari (Procore Technologies)",
 "note": "Most developers use AI the same way: open a chat, type a prompt, move on."}
```

#### What's next with GitHub Next: tomorrow's tools for making software

**Wednesday, Oct 28 · 12:30 PM - 1:10 PM PDT**  
**Where:** Silent Disco Breakouts @ Festival Pavilion  
**Type:** Breakout Session · **Format:** In-person, AI summary

GitHub Next is the labs team of GitHub, scouting the future of software with the goal of making all development faster, safer, easier, and more accessible to more people. Beyond creating GitHub Copilot, Next has been at the forefront of every shift in software development: AI completions, spec-based programming, natural-language-to-app, automation, and more.

Join us for a tour of the lab! See demos of the explorations we're conducting, and learn how Next thinks about the future of software development. Some of it will be weird, some of it will be wrong, and some of it will be wonderful.

**Speakers**

- Idan Gazit: Head of GitHub Next, GitHub
- Maggie Appleton: Staff Research Engineer, GitHub

```json
{"day": "2026-10-28", "start": "12:30", "end": "13:10",
 "title": "What's next with GitHub Next: tomorrow's tools for making software", "room": "Silent Disco Breakouts",
 "speaker": "Idan Gazit (GitHub), Maggie Appleton (GitHub)",
 "note": "Join us for a tour of the lab!"}
```

### 12:50 PM

#### The factory mindset: Agentic workflows in production

**Wednesday, Oct 28 · 12:50 PM - 1:20 PM PDT**  
**Where:** Main Stage @ Festival Pavilion  
**Type:** Main Stage · **Format:** In-person, Recorded, AI summary

A factory isn't defined by what it produces. It's defined by the process that produces it. The GitHub Agentic Workflows team built one: five engineers, GitHub Actions as the floor, agents as the crew, 460 pull requests a week. Peli de Halleux from the GitHub Next team shows you how it's wired. Marks & Spencer shows how it scales: from a proof-of-concept that raised 123 issues and fixed 77 the same day, to a central control plane deploying governed workflows across the organization. Provation brings the regulated perspective: what it looks like to adopt agentic development in healthcare, where every automated decision needs an audit trail, and how it can strengthen an already mature compliance program.

You'll leave knowing how an agentic development factory comes together, what it takes to run one, and how teams across retail, healthcare, and beyond are putting it to work today.

**Speakers**

- Peli de Halleux: Agentic Engineer, GitHub Next, Microsoft
- Paul Snider: CTO, Provation / Fortive
- Tim Mason: Principal Engineer, Marks and Spencer

```json
{"day": "2026-10-28", "start": "12:50", "end": "13:20",
 "title": "The factory mindset: Agentic workflows in production", "room": "Main Stage",
 "speaker": "Peli de Halleux (Microsoft), Paul Snider (Provation / Fortive), Tim Mason (Marks and Spencer)",
 "note": "You'll leave knowing how an agentic development factory comes together, what it takes to run one, and how teams across retail..."}
```

#### Capture the flag: Three AI teams, one codebase, zero mercy

**Wednesday, Oct 28 · 12:50 PM - 1:35 PM PDT**  
**Where:** Sandbox @ Fort Mason Building C, Founders Inc., 3rd Floor  
**Type:** Sandbox Session · **Format:** In-person

Capture the flag is the most iconic format in cybersecurity, so we turned it into a live GitHub battle. Three squads of AI agents compete on the same codebase in real time: a Dev Team ships features, a Red Team sneaks in vulnerabilities, and a Blue Team hunts them down with GitHub Advanced Security as the referee.

The agents run on Squad (by Brady Gaster), and Pixel Agents makes their every move visible on screen. You won't just hear about agentic workflows and security controls at enterprise scale, you'll watch them collide, live.

You'll leave knowing which GitHub security controls are non-negotiable for AI-generated code and with the open source repo to run the match yourself.

**Speakers**

- Christophe Crémon: Forward Deployed Engineer - Agentic AI, Onepoint
- Romain Le Disez: FDA & Alliance Lead, Onepoint

```json
{"day": "2026-10-28", "start": "12:50", "end": "13:35",
 "title": "Capture the flag: Three AI teams, one codebase, zero mercy", "room": "Sandbox, 3rd Floor",
 "speaker": "Christophe Cr\u00e9mon (Onepoint), Romain Le Disez (Onepoint)",
 "note": "You'll leave knowing which GitHub security controls are non-negotiable for AI-generated code and with the open source repo to run the..."}
```

### 1:00 PM

#### Building a developer knowledge base for GitHub Copilot

**Wednesday, Oct 28 · 1:00 PM - 2:30 PM PDT**  
**Where:** Workshops @ Gateway Pavilion, Level 1  
**Type:** Workshop · **Format:** In-person

Give GitHub Copilot access to the knowledge your team already has, without rewriting any of it. In this interactive, 90-minute workshop, you'll build a developer knowledge base from the artifacts your team already produces: issues, PRs, docs, and discussions. You'll ingest that content, tune it for retrieval, and expose it through an MCP server so Copilot can use it directly.

From there, you'll use the GitHub Copilot CLI to query your knowledge base inside real workflows, producing grounded summaries and actionable pointers that link straight back to the source issues, PRs, and docs. 

You'll leave with a working knowledge base, the retrieval and MCP setup behind it, and a repeatable pattern for grounding Copilot in your own team's knowledge, ready to adapt to your real repositories.

**Speakers**

- Pamela Fox: Principal Cloud Advocate in Python, Microsoft
- Said Nikjou: Sr. Cloud Solution Architect, Microsoft

```json
{"day": "2026-10-28", "start": "13:00", "end": "14:30",
 "title": "Building a developer knowledge base for GitHub Copilot", "room": "Workshops (Level 1)",
 "speaker": "Pamela Fox (Microsoft), Said Nikjou (Microsoft)",
 "note": "You'll leave with a working knowledge base, the retrieval and MCP setup behind it, and a repeatable pattern for grounding Copilot in..."}
```

### 1:10 PM

#### Stop waiting on your own pull requests: GitHub Stacked PRs in practice

**Wednesday, Oct 28 · 1:10 PM - 1:25 PM PDT**  
**Where:** Silent Disco Demos @ Festival Pavilion  
**Type:** Product Demo · **Format:** In-person, Recorded, AI summary

Big pull requests slow everyone down. Reviewers stall on large diffs, authors lose flow waiting on dependent work, and feedback loops stretch from hours to days. GitHub Stacked PRs let you split changes into smaller, dependent pull requests that move through review efficiently while preserving the full picture. 

In this demo, Sameen Karim (part of the team that built Stacked PRs) builds a stack with the GitHub CLI, reviews it on github.com, and merges each pull request as soon as it's ready. You'll leave with a workflow you can use on your team's repository tomorrow.

**Speakers**

- Sameen Karim: Senior Product Manager, GitHub

```json
{"day": "2026-10-28", "start": "13:10", "end": "13:25",
 "title": "Stop waiting on your own pull requests: GitHub Stacked PRs in practice", "room": "Silent Disco Demos",
 "speaker": "Sameen Karim (GitHub)",
 "note": "Sameen Karim (part of the team that built Stacked PRs) builds a stack with the GitHub CLI, reviews it on github.com, and merges each..."}
```

### 1:30 PM

#### How to go from alert to pull request in minutes: Wiring NeuBird and Copilot via MCP (Sponsored)

**Wednesday, Oct 28 · 1:30 PM - 1:45 PM PDT**  
**Where:** Silent Disco Demos @ Festival Pavilion  
**Type:** Product Demo · **Format:** In-person, Recorded, AI summary

Getting paged at 2 a.m., manually correlating logs across 15 dashboards, drafting a fix under pressure... that's the current state of incident response for most teams. This live demo shows a different model: NeuBird's Production Ops Agent investigates the alert and produces a structured root cause analysis (RCA). That RCA becomes the input payload for GitHub Copilot via MCP: Copilot generates a targeted fix, runs it through security scanning and tests, and opens a fully documented pull request.

Grant Griffiths shows what it takes to wire two AI agents together via MCP, what the handoff object actually looks like, and where it breaks down in practice. You'll leave with a concrete architecture for multi-agent incident resolution and a realistic picture of what works today.

**Speakers**

- Grant Griffiths: Founding Engineer, NeuBird AI

```json
{"day": "2026-10-28", "start": "13:30", "end": "13:45",
 "title": "How to go from alert to pull request in minutes: Wiring NeuBird and Copilot via MCP (Sponsored)", "room": "Silent Disco Demos",
 "speaker": "Grant Griffiths (NeuBird AI)",
 "note": "You'll leave with a concrete architecture for multi-agent incident resolution and a realistic picture of what works today."}
```

#### Accelerate accessibility with AI and automation

**Wednesday, Oct 28 · 1:30 PM - 2:10 PM PDT**  
**Where:** BATS Theatre @ Fort Mason Building B, 3rd Floor  
**Type:** Panel Discussion · **Format:** In-person, AI summary

Accessibility has become a hard requirement for many organizations, but out-of-the-box AI code suggestions frequently miss the mark. So what's a developer to do?

Join a panel of accessibility experts for a practical update on how to use AI and automation to accelerate accessibility, not undermine it. They'll cover where AI genuinely helps, where it still falls short, and the current best practices for combining automated tooling with human judgment to build accessible software.

You'll leave with actionable tips you can apply right away, whether you're improving accessibility, reducing legal risk, or expanding your customer base by reaching more users.

**Speakers**

- Eric Bailey: Accessibility advocate, Independent
- Ed Summers: Head of Accessibility, GitHub
- Michael Fairchild: Accessibility engineer, Independent
- Maya Shavin: Staff Software Engineer, Salesforce

```json
{"day": "2026-10-28", "start": "13:30", "end": "14:10",
 "title": "Accelerate accessibility with AI and automation", "room": "BATS Theatre, 3rd Floor",
 "speaker": "Eric Bailey (Independent), Ed Summers (GitHub), Michael Fairchild (Independent), Maya Shavin (Salesforce)",
 "note": "Join a panel of accessibility experts for a practical update on how to use AI and automation to accelerate accessibility, not undermine it."}
```

#### Agent-driven deployment beyond localhost, shared securely with your team (Sponsored)

**Wednesday, Oct 28 · 1:30 PM - 2:10 PM PDT**  
**Where:** Silent Disco Breakouts @ Festival Pavilion  
**Type:** Breakout Session · **Format:** In-person, AI summary

You and your agent just built something that works on your laptop. Now you want your team to use it, without exposing it to the whole internet or wrestling with passwords and credentials to lock it down. In this demo, you simply ask your agent to publish it, and it handles the rest: opening a pull request, deploying the app, and putting it behind private, identity-based access that only you can reach. Sharing it with your team is just as easy, and every change to who can get in is captured in a diff you approve. The result is a way to ship and share work that's private by default, where identity decides who gets access and the review trail records why. You'll leave knowing how agents can take your work from localhost to your team securely, without public URLs, shared passwords, or credentials to manage.

**Speakers**

- Kartik Bharath: Solutions Engineer, Tailscale

```json
{"day": "2026-10-28", "start": "13:30", "end": "14:10",
 "title": "Agent-driven deployment beyond localhost, shared securely with your team (Sponsored)", "room": "Silent Disco Breakouts",
 "speaker": "Kartik Bharath (Tailscale)",
 "note": "You simply ask your agent to publish it, and it handles the rest: opening a pull request, deploying the app, and putting it behind..."}
```

### 1:35 PM

#### Session After Party: The factory mindset: Agentic workflows in production

**Wednesday, Oct 28 · 1:35 PM - 2:05 PM PDT**  
**Where:** The Speakeasy @ GitHub Central, Festival Pavilion  
**Type:** Session After Party · **Format:** In-person

This is an informal follow-up Q&A to the main stage session "The factory mindset: Agentic workflows in production." Right after the talk, join Peli de Halleux (GitHub Next), Tim Mason (Marks & Spencer), and Paul Snider (Provation) in GitHub Central. Bring your questions and keep the conversation going.

**Speakers**

- Peli de Halleux: Agentic Engineer, GitHub Next, Microsoft
- Tim Mason: Principal Engineer, Marks and Spencer
- Paul Snider: CTO, Provation / Fortive

```json
{"day": "2026-10-28", "start": "13:35", "end": "14:05",
 "title": "Session After Party: The factory mindset: Agentic workflows in production", "room": "The Speakeasy (GitHub Central)",
 "speaker": "Peli de Halleux (Microsoft), Tim Mason (Marks and Spencer), Paul Snider (Provation / Fortive)",
 "note": "This is an informal follow-up Q&A to the main stage session \"The factory mindset: Agentic workflows in production.\" Right after the..."}
```

### 1:40 PM

#### The O(1) patch: Securing the supply chain against AI-discovered zero-days

**Wednesday, Oct 28 · 1:40 PM - 1:55 PM PDT**  
**Where:** Ship & Tell @ Firehouse  
**Type:** Ship & Tell · **Format:** In-person, Recorded, AI summary

AI models can now autonomously discover decades-old CVEs, which means the software supply chain has never been more fragile. When the next zero-day drops, scanning your infrastructure node-by-node with non-deterministic package managers is an O(n) problem: by the time you know where you're exposed, you're already too late.

This session explores a different foundation. By shifting to deterministic package management — built on the principles of NixOS and nixpkgs — CVE detection and remediation become an O(1) lookup against a fixed, cryptographic manifest of exactly what's in your system. Instead of asking "are we affected?" and scanning to find out, you already know, instantly and provably.

You'll leave understanding what "secure by construction" really means, how deterministic builds change your exposure model when a zero-day hits, and what it takes to move toward this approach in a real supply chain.

**Speakers**

- Ron Efroni: CEO and Co-Founder, Flox and NixOS

```json
{"day": "2026-10-28", "start": "13:40", "end": "13:55",
 "title": "The O(1) patch: Securing the supply chain against AI-discovered zero-days", "room": "Ship & Tell",
 "speaker": "Ron Efroni (Flox and NixOS)",
 "note": "This session explores a different foundation."}
```

#### Work together, your way, with GitHub Copilot

**Wednesday, Oct 28 · 1:40 PM - 2:10 PM PDT**  
**Where:** Main Stage @ Festival Pavilion  
**Type:** Main Stage · **Format:** In-person, Recorded, AI summary

Your team might agree on what to build, but how to build it is another conversation. Join Pierce Boggan and team as they tackle a shared project with GitHub Copilot, bringing their favorite tools, models, and a few strong opinions. Working across the Copilot app, CLI, VS Code, and JetBrains, they’ll put agents to work, carry context between tasks, and take development beyond the editor, balancing speed, cost, and control a little differently. Follow the project from idea to working software to see how the latest in Copilot helps a team build together without making everyone work the same way.

**Speakers**

- Burke Holland: Principal Cloud Advocate, Microsoft
- James Montemagno: Principal Technical PM Lead, Microsoft
- Pierce Boggan: Product - GitHub Copilot, GitHub
- Julia Kasper: Product Manager, Microsoft
- Katie Savage: Technical Program Manager, Microsoft

```json
{"day": "2026-10-28", "start": "13:40", "end": "14:10",
 "title": "Work together, your way, with GitHub Copilot", "room": "Main Stage",
 "speaker": "Burke Holland (Microsoft), James Montemagno (Microsoft), Pierce Boggan (GitHub), Julia Kasper (Microsoft), Katie Savage (Microsoft)",
 "note": "Join Pierce Boggan and team as they tackle a shared project with GitHub Copilot, bringing their favorite tools, models, and a few strong..."}
```

### 1:45 PM

#### What does shift left mean in an agentic world? (Sponsored)

**Wednesday, Oct 28 · 1:45 PM - 2:00 PM PDT**  
**Where:** Demos & Donuts @ Gateway Pavilion, Level 2  
**Type:** Product Demo · **Format:** In-person, AI summary

Coding agents can read our repositories, write code, run commands, and increasingly act across the delivery lifecycle. But they often know far more about how a system is built than how it actually behaves. This talk explores what shift left observability means when agents are part of the development workflow: bringing operational evidence into their decisions, making those decisions reviewable, and keeping authority and verification in place before a plausible guess becomes a real change. You'll leave with a clearer sense of how to give your agents the operational context they're missing, and how to keep humans in the loop before a guess ships to production.

**Speakers**

- Spencer Taylor: Principal Developer Relations Engineer, New Relic

```json
{"day": "2026-10-28", "start": "13:45", "end": "14:00",
 "title": "What does shift left mean in an agentic world? (Sponsored)", "room": "Demos & Donuts (Level 2)",
 "speaker": "Spencer Taylor (New Relic)",
 "note": "This talk explores what shift left observability means when agents are part of the development workflow: bringing operational evidence..."}
```

### 1:50 PM

#### Auth for agents: How auth.md lets agents skip the sign-up form (Sponsored)

**Wednesday, Oct 28 · 1:50 PM - 2:05 PM PDT**  
**Where:** Silent Disco Demos @ Festival Pavilion  
**Type:** Product Demo · **Format:** In-person, Recorded, AI summary

Every AI agent hits the same wall: to act on a user's behalf, someone still has to create an account, generate an API key, and paste it into a config file. auth.md is WorkOS's open protocol for skipping that step. Services publish a lightweight auth.md file pointing agents to a standard discovery document. From there, an agent that already knows who its user is can exchange that identity for scoped, short-lived credentials to your API. No signup form, no copied API key, no separate developer console.

In this live demo, WorkOS will show auth.md end-to-end: an agent discovering support for the protocol, asserting a user's identity, and getting back scoped credentials it can use immediately — plus what it takes to add auth.md support to your own API.

You'll leave understanding how the protocol works under the hood, why identity-based credential exchange is safer than long-lived API keys, and how to publish your own auth.md file so any agent can authenticate to your API without a single copied secret.

**Speakers**

- Michael Grinich: CEO, WorkOS

```json
{"day": "2026-10-28", "start": "13:50", "end": "14:05",
 "title": "Auth for agents: How auth.md lets agents skip the sign-up form (Sponsored)", "room": "Silent Disco Demos",
 "speaker": "Michael Grinich (WorkOS)",
 "note": "You'll leave understanding how the protocol works under the hood, why identity-based credential exchange is safer than long-lived API..."}
```

### 2:05 PM

#### Automate the everyday with Copilot Automations

**Wednesday, Oct 28 · 2:05 PM - 2:20 PM PDT**  
**Where:** Demos & Donuts @ Gateway Pavilion, Level 2  
**Type:** Product Demo · **Format:** In-person, AI summary

AI can speed up coding, but repetitive work across the software lifecycle can still slow teams down. In this live demo, you’ll see how developers can give Copilot clear instructions to help with recurring engineering work. Explore practical examples such as triaging issues and investigating production errors. Leave with ideas for reducing repetitive work and keeping software moving.

**Speakers**

- Tim Rogers: Principal Product Manager, GitHub

```json
{"day": "2026-10-28", "start": "14:05", "end": "14:20",
 "title": "Automate the everyday with Copilot Automations", "room": "Demos & Donuts (Level 2)",
 "speaker": "Tim Rogers (GitHub)",
 "note": "Explore practical examples such as triaging issues and investigating production errors."}
```

### 2:10 PM

#### Bringing AI-detected secret scanning to push time and on-prem environments

**Wednesday, Oct 28 · 2:10 PM - 2:25 PM PDT**  
**Where:** Silent Disco Demos @ Festival Pavilion  
**Type:** Product Demo · **Format:** In-person, Recorded, AI summary

Secret detection has a four-body problem: confidence, speed, performance under load, and cost. Pattern matching is fast and cheap, but it misses the long tail of credentials without recognizable formats. Hosted LLMs catch more, but they aren’t built for the critical path of every push — where every decision has a sub-second latency budget — or for air-gapped GitHub Enterprise Server (GHES) environments, where the model has to run on-premises instead of calling out to a hosted LLM.

In this demo, you’ll see GitHub’s AI-powered secret scanning bring secrets to two new surfaces: push protection, where unstructured credentials are blocked before they land in a repository, and GHES, where the same detection runs fully on-premises with no hosted LLM required.

You’ll leave knowing how GitHub detects secrets at push time and on-premises: intelligent enough to catch what pattern matching misses, fast enough to run on every push, and portable enough for air-gapped GHES.

**Speakers**

- Erin Havens: Senior Product Manager, GitHub

```json
{"day": "2026-10-28", "start": "14:10", "end": "14:25",
 "title": "Bringing AI-detected secret scanning to push time and on-prem environments", "room": "Silent Disco Demos",
 "speaker": "Erin Havens (GitHub)",
 "note": "You'll see GitHub's AI-powered secret scanning bring secrets to two new surfaces: push protection, where unstructured credentials are..."}
```

#### Code is the easy part: Building Home Assistant in the open

**Wednesday, Oct 28 · 2:10 PM - 2:25 PM PDT**  
**Where:** Ship & Tell @ Firehouse  
**Type:** Ship & Tell · **Format:** In-person, Recorded, AI summary

"Building in the open" usually means one thing: code on GitHub. As engineers, the Home Assistant team will tell you that's the easy part. The hard work starts long before code — ideas, UX, design, architecture, the roadmap itself — and at Home Assistant, all of it happens on GitHub, across 20,000 contributors, hundreds of repositories, and a dozen GitHub organizations.

This session shows how the Open Home Foundation runs its entire roadmap in the open, using what Issues, Projects, and Discussions have become over the last two years. You'll see how feature requests get debated in Discussions, how scoping happens in Issues with sub-issues and custom fields, and how a living roadmap in Projects lets anyone comment, steer it, pick up an item, and ship it. 

You'll also see the harder parts: being wrong in public and fixing it in public, and iterating with the community before any code is written. Because you don't have to be technical to contribute: every single person can, even with a comment, before a line of code exists. That's building in the open.

**Speakers**

- Franck Nijhof: Lead of Home Assistant, Open Home Foundation

```json
{"day": "2026-10-28", "start": "14:10", "end": "14:25",
 "title": "Code is the easy part: Building Home Assistant in the open", "room": "Ship & Tell",
 "speaker": "Franck Nijhof (Open Home Foundation)",
 "note": "This session shows how the Open Home Foundation runs its entire roadmap in the open, using what Issues, Projects, and Discussions have..."}
```

### 2:20 PM

#### Expand Copilot beyond coding: Non-code workflows your team isn't using yet

**Wednesday, Oct 28 · 2:20 PM - 3:05 PM PDT**  
**Where:** Sandbox @ Fort Mason Building C, Founders Inc., 3rd Floor  
**Type:** Sandbox Session · **Format:** In-person

Your team uses GitHub Copilot to write code. But what about the hours spent on project planning, documentation, recurring reports, and cross-team coordination? Those workflows respond to the same agentic tools, and most engineering leaders haven't expanded Copilot there yet.

In this Sandbox session, Grace Vorreuter and Jenny Hwang demo non-coding workflows in the GitHub Copilot App, from triaging feedback and automating recurring reports to turning team discussions into ready-to-go work. Come try it yourself in guided exercises!

You'll leave with repeatable patterns for non-code workflows and a clear picture of how to expand Copilot adoption across your team beyond traditional development tasks.

**Speakers**

- Grace Vorreuter: Principal User Researcher, GitHub
- Jenny Hwang: Director of Product Research, GitHub

```json
{"day": "2026-10-28", "start": "14:20", "end": "15:05",
 "title": "Expand Copilot beyond coding: Non-code workflows your team isn't using yet", "room": "Sandbox, 3rd Floor",
 "speaker": "Grace Vorreuter (GitHub), Jenny Hwang (GitHub)",
 "note": "You'll leave with repeatable patterns for non-code workflows and a clear picture of how to expand Copilot adoption across your team..."}
```

### 2:25 PM

#### Build a self-validating agentic loop with GitHub Copilot (Sponsored)

**Wednesday, Oct 28 · 2:25 PM - 2:40 PM PDT**  
**Where:** Demos & Donuts @ Gateway Pavilion, Level 2  
**Type:** Product Demo · **Format:** In-person, AI summary

AI agents are writing more of your codebase every day, and they're confident in every line. But confidence is not correctness, and trust is what ships. In this live demo, build a self-validating agentic loop with GitHub Copilot, where the same flow that writes your code also proves it works. Follow one pull request from end to end: use cases become tests, coverage is measured live, and tests are authored in VS Code and scaled in parallel through GitHub Actions. By the end, Copilot posts clear, human-readable proof right on the pull request. That's how confidence becomes trust, and you'll leave knowing how to build a loop where speed and accuracy work as one.

**Speakers**

- Shravan Mahajan: Software Engineer, TestMu AI
- Siddhant Sinha: Lead Member, Technical Staff, TestMu AI

```json
{"day": "2026-10-28", "start": "14:25", "end": "14:40",
 "title": "Build a self-validating agentic loop with GitHub Copilot (Sponsored)", "room": "Demos & Donuts (Level 2)",
 "speaker": "Shravan Mahajan (TestMu AI), Siddhant Sinha (TestMu AI)",
 "note": "AI agents are writing more of your codebase every day, and they're confident in every line."}
```

#### Session After Party: Work together, your way, with GitHub Copilot

**Wednesday, Oct 28 · 2:25 PM - 2:55 PM PDT**  
**Where:** The Speakeasy @ GitHub Central, Festival Pavilion  
**Type:** Session After Party · **Format:** In-person

This is an informal follow-up Q&A to the main stage session "Work together, your way, with GitHub Copilot." Right after the talk, join the speakers in GitHub Central. Bring your questions and keep the conversation going.

**Speakers**

- James Montemagno: Principal Technical PM Lead, Microsoft
- Burke Holland: Principal Cloud Advocate, Microsoft
- Pierce Boggan: Product - GitHub Copilot, GitHub
- Julia Kasper: Product Manager, Microsoft
- Katie Savage: Technical Program Manager, Microsoft

```json
{"day": "2026-10-28", "start": "14:25", "end": "14:55",
 "title": "Session After Party: Work together, your way, with GitHub Copilot", "room": "The Speakeasy (GitHub Central)",
 "speaker": "James Montemagno (Microsoft), Burke Holland (Microsoft), Pierce Boggan (GitHub), Julia Kasper (Microsoft), Katie Savage (Microsoft)",
 "note": "This is an informal follow-up Q&A to the main stage session \"Work together, your way, with GitHub Copilot.\" Right after the talk, join..."}
```

### 2:30 PM

#### Day 1 deploy, day 2 recovery: AI agents across the full delivery lifecycle (Sponsored)

**Wednesday, Oct 28 · 2:30 PM - 2:45 PM PDT**  
**Where:** Silent Disco Demos @ Festival Pavilion  
**Type:** Product Demo · **Format:** In-person, Recorded, AI summary

In this live demo, James Chatmas follows that developer from Day 1 to Day 2. First, an AI agent helps create a governed Octopus deployment process and complete the first successful deployment. Then, when a later deployment fails, the Octopus Intelligence Agent diagnoses the issue, runs the approved remediation, and redeploys, all from GitHub. You'll see how human approvals, runbooks, and deployment controls let teams automate recovery without sacrificing governance.

**Speakers**

- James Chatmas: Principal Solutions Engineer, Octopus Deploy

```json
{"day": "2026-10-28", "start": "14:30", "end": "14:45",
 "title": "Day 1 deploy, day 2 recovery: AI agents across the full delivery lifecycle (Sponsored)", "room": "Silent Disco Demos",
 "speaker": "James Chatmas (Octopus Deploy)",
 "note": "You'll see how human approvals, runbooks, and deployment controls let teams automate recovery without sacrificing governance."}
```

#### Disrupting supply chain attacks: A threat framework for GitHub Actions

**Wednesday, Oct 28 · 2:30 PM - 3:00 PM PDT**  
**Where:** Main Stage @ Festival Pavilion  
**Type:** Main Stage · **Format:** In-person, Recorded, AI summary

Recent attacks on open source projects have grown more frequent and sophisticated, exposing a hard truth: adversaries are targeting CI/CD itself, not just the code it ships. Pipelines hold credentials, access networks, and release software across ecosystems, making them prime targets for attackers seeking to spread malware. 

This session walks through a threat framework for software supply chain attacks, maps each technique to the GitHub Actions controls available today, and shows where Actions security is headed. You'll see how GitHub is hardening Actions across three layers: the ecosystem, the workflow attack surface, and the runner infrastructure.

**Speakers**

- Steve Glass: Senior Product Manager, GitHub
- Greg Ose: Principal Product Security Engineer, GitHub

```json
{"day": "2026-10-28", "start": "14:30", "end": "15:00",
 "title": "Disrupting supply chain attacks: A threat framework for GitHub Actions", "room": "Main Stage",
 "speaker": "Steve Glass (GitHub), Greg Ose (GitHub)",
 "note": "This session walks through a threat framework for software supply chain attacks, maps each technique to the GitHub Actions controls..."}
```

#### Agentic security for every developer

**Wednesday, Oct 28 · 2:30 PM - 3:10 PM PDT**  
**Where:** Silent Disco Breakouts @ Festival Pavilion  
**Type:** Breakout Session · **Format:** In-person, AI summary

The security landscape shifted dramatically in 2026: rising AI capabilities put sophisticated attacks within reach of far more threat actors, and with development accelerating rapidly, traditional security tools struggle to keep pace.

Join GitHub's Security Products leaders for a first look at a new wave of agentic security tooling — now available to every developer, everywhere they work, from the CLI to the App to GitHub itself. It's built to find and fix the risks that matter most, now.

You'll get an early look at where GitHub is taking agentic security, see it in action across your workflow, and leave understanding what it means to have an agent working on your security alongside you.

**Speakers**

- Pierre Tempel: Director, Product Management, GitHub
- Ying Chang: Sr. Product Manager, Microsoft

```json
{"day": "2026-10-28", "start": "14:30", "end": "15:10",
 "title": "Agentic security for every developer", "room": "Silent Disco Breakouts",
 "speaker": "Pierre Tempel (GitHub), Ying Chang (Microsoft)",
 "note": "Join GitHub's Security Products leaders for a first look at a new wave of agentic security tooling - now available to every developer..."}
```

#### Beyond "hours saved": How AMD and ING measure AI at enterprise scale

**Wednesday, Oct 28 · 2:30 PM - 3:10 PM PDT**  
**Where:** Cowell Theater @ Gateway Pavilion  
**Type:** Breakout Session · **Format:** In-person, AI summary

Measuring AI impact takes more than tracking suggestions accepted or hours saved. As organizations move from experimentation to enterprise rollout, the question shifts: how do you connect AI investments to actual engineering and business outcomes?

In this session, Eric Hollenberry (GitHub), Alex Androncik (AMD), and Jeffrey Opdam (ING) share what they've learned by: 
-Evaluating GitHub Copilot across thousands of engineers using controlled pilots, engineering metrics, and behavioral data — and using the results to shape their enterprise rollout. 
-Evolving their AI platforms to measure efficiency, optimize cost, and tie AI spend to product outcomes. 

You'll leave knowing which metrics matter at different stages of adoption, where measurement is still evolving, and practical lessons for building a measurement strategy that moves with your organization.

**Speakers**

- Jeffrey Opdam: Architect, ING
- Eric Hollenberry: Principal Product Manager, Metrics, GitHub
- Alexander Androncik: Corp. VP, Applied AI, Advanced Micro Devices (AMD)

```json
{"day": "2026-10-28", "start": "14:30", "end": "15:10",
 "title": "Beyond \"hours saved\": How AMD and ING measure AI at enterprise scale", "room": "Cowell Theater",
 "speaker": "Jeffrey Opdam (ING), Eric Hollenberry (GitHub), Alexander Androncik (Advanced Micro Devices (AMD))",
 "note": "Eric Hollenberry (GitHub), Alex Androncik (AMD), and Jeffrey Opdam (ING) share what they've learned by: -Evaluating GitHub Copilot..."}
```

#### One PM, four weeks, full compliance: How itti shipped a banking product with agents

**Wednesday, Oct 28 · 2:30 PM - 3:10 PM PDT**  
**Where:** BATS Theatre @ Fort Mason Building B, 3rd Floor  
**Type:** Breakout Session · **Format:** In-person, AI summary

Ueno Ads, an in-app advertising product for the UENO banking platform, was scoped as a six-month build with a full delivery squad: product, engineering leadership, UX, developers, and QA. The team at itti shipped it in four weeks, with one product manager directing agents on GitHub. 

Inside a regulated bank, that only holds up if a person can approve and trace every step. Javier Durán and Leonardo Esteban Villa show the pipeline itti built to make that true, the gates that got it through cybersecurity review, and where the bottleneck moved once agents were doing the writing. You'll leave knowing where humans need to stay in the loop and what it takes for agent-written work to survive a security review.

**Speakers**

- Javier Durán: Senior Manager AI, itti (Grupo Vázquez)
- Leonardo Esteban Villa: Tech Lead Venture, itti

```json
{"day": "2026-10-28", "start": "14:30", "end": "15:10",
 "title": "One PM, four weeks, full compliance: How itti shipped a banking product with agents", "room": "BATS Theatre, 3rd Floor",
 "speaker": "Javier Dur\u00e1n (itti (Grupo V\u00e1zquez)), Leonardo Esteban Villa (itti)",
 "note": "You'll leave knowing where humans need to stay in the loop and what it takes for agent-written work to survive a security review."}
```

### 2:40 PM

#### Who's watching the agents? What AI code does in production

**Wednesday, Oct 28 · 2:40 PM - 2:55 PM PDT**  
**Where:** Ship & Tell @ Firehouse  
**Type:** Ship & Tell · **Format:** In-person, Recorded, AI summary

GitHub Copilot and coding agents can now write, commit, and deploy code autonomously, and GitHub gives you a powerful control plane over how that software is created and shipped. But once the code runs in production, its behavior gets much harder to see. Static analysis and PR review can inspect code at rest; neither can observe a running process.

This session shows how eBPF-based runtime observability extends that model down into the kernel, giving you visibility into the processes, file access, and network activity of AI-generated workloads as they actually execute. When an agent's code reaches out to an unexpected endpoint or touches a file it shouldn't, you see it.

You'll leave with a practical way to close the security loop that AI introduces: not just reviewing what agents write, but watching what their code actually does once it's live.

**Speakers**

- Donia Chaiehloudj: Senior Software Engineer, Isovalent part of Cisco

```json
{"day": "2026-10-28", "start": "14:40", "end": "14:55",
 "title": "Who's watching the agents? What AI code does in production", "room": "Ship & Tell",
 "speaker": "Donia Chaiehloudj (Isovalent part of Cisco)",
 "note": "This session shows how eBPF-based runtime observability extends that model down into the kernel, giving you visibility into the..."}
```

### 2:45 PM

#### Turning user feedback into requirements with a custom Copilot agent

**Wednesday, Oct 28 · 2:45 PM - 3:00 PM PDT**  
**Where:** Demos & Donuts @ Gateway Pavilion, Level 2  
**Type:** Product Demo · **Format:** In-person, AI summary

AI-assisted tools make it easier than ever for more people to turn ideas into working software. But while the barrier to building is falling, the need to evaluate ideas and validate assumptions in order to build the right experience remains. This GitHub App demo shows how an agent can connect feedback signals across multiple channels, creating a unified view of customer needs that helps teams prioritize opportunities, shape requirements, and make more informed product decisions.

**Speakers**

- Kristin N. Dew: Senior Researcher, GitHub
- Catharine McNally: Staff Program Manager, GitHub

```json
{"day": "2026-10-28", "start": "14:45", "end": "15:00",
 "title": "Turning user feedback into requirements with a custom Copilot agent", "room": "Demos & Donuts (Level 2)",
 "speaker": "Kristin N. Dew (GitHub), Catharine McNally (GitHub)",
 "note": "AI-assisted tools make it easier than ever for more people to turn ideas into working software."}
```

### 2:50 PM

#### Going beyond suggestions: How to govern agentic workflows in GitHub (Sponsored)

**Wednesday, Oct 28 · 2:50 PM - 3:05 PM PDT**  
**Where:** Silent Disco Demos @ Festival Pavilion  
**Type:** Product Demo · **Format:** In-person, Recorded, AI summary

Not every engineering task arrives with a clear set of steps. GitHub Agentic Workflows can interpret the situation, decide what to do next, and take action, extending automation to work that usually starts with human triage. That flexibility creates a new challenge: how do teams give agents room to help while keeping permissions, security, and review under human control? 

This session explains the guardrails that make agent-powered workflows manageable, including scoped permissions, workflow governance, safe execution patterns, and review of agent contributions. Through architecture diagrams and workflow examples, you’ll see how teams can use agents to analyze code, maintain repositories, and handle repetitive work without giving them unrestricted access. 

You’ll leave with a practical framework for deciding what an agent can do, what it needs a person to approve, and how to keep its actions secure and auditable.

**Speakers**

- Dave Benedic: Sr. Manager - Agentic Platforms, Insight
- Parker Johnston: Agentic Field CTO, Insight

```json
{"day": "2026-10-28", "start": "14:50", "end": "15:05",
 "title": "Going beyond suggestions: How to govern agentic workflows in GitHub (Sponsored)", "room": "Silent Disco Demos",
 "speaker": "Dave Benedic (Insight), Parker Johnston (Insight)",
 "note": "This session explains the guardrails that make agent-powered workflows manageable, including scoped permissions, workflow governance..."}
```

### 3:05 PM

#### Keep vulnerabilities out of your codebase, without leaving where you build

**Wednesday, Oct 28 · 3:05 PM - 3:20 PM PDT**  
**Where:** Demos & Donuts @ Gateway Pavilion, Level 2  
**Type:** Product Demo · **Format:** In-person, AI summary

Vulnerabilities reach developers from two directions. New code arrives faster than ever, and better scanning uncovers old flaws in code merged long ago. Both usually land on a security tab, away from where you work. In this demo, we'll show how developers building with agents can move security ahead of the code. You'll see how to review what you and your agents just wrote, including uncommitted changes, and fix issues before a pull request exists. Then we'll bring your repository's existing alerts into the same place, where Copilot can explain them, turn a long list into a clear fix-first plan and help you fix them as you build.

**Speakers**

- James Fletcher: Senior Product Manager, GitHub

```json
{"day": "2026-10-28", "start": "15:05", "end": "15:20",
 "title": "Keep vulnerabilities out of your codebase, without leaving where you build", "room": "Demos & Donuts (Level 2)",
 "speaker": "James Fletcher (GitHub)",
 "note": "We'll show how developers building with agents can move security ahead of the code."}
```

### 3:10 PM

#### How to shift specifications from contracts to hypotheses

**Wednesday, Oct 28 · 3:10 PM - 3:25 PM PDT**  
**Where:** Ship & Tell @ Firehouse  
**Type:** Ship & Tell · **Format:** In-person, Recorded, AI summary

Teams building agents and workflows powered by GitHub Copilot are inheriting a habit that quietly breaks: writing specifications as contracts. A traditional spec is binding. But AI doesn't work that way. The same prompt produces different outputs across runs, models, and updates. If you over-trust the spec, you risk shipping features that "passed" while doing the wrong thing. Abandon specs entirely, and you lose control. 

In this session, Julio Arruda walks through two real production failures caused by this pattern, then introduces a working reframe. You'll leave with a three-practice checklist you can apply Monday.

**Speakers**

- Julio Arruda: Chief Architect, GFT Technologies

```json
{"day": "2026-10-28", "start": "15:10", "end": "15:25",
 "title": "How to shift specifications from contracts to hypotheses", "room": "Ship & Tell",
 "speaker": "Julio Arruda (GFT Technologies)",
 "note": "Julio Arruda walks through two real production failures caused by this pattern, then introduces a working reframe."}
```

#### How to think about reachability and use it to prioritize vulnerabilities

**Wednesday, Oct 28 · 3:10 PM - 3:25 PM PDT**  
**Where:** Silent Disco Demos @ Festival Pavilion  
**Type:** Product Demo · **Format:** In-person, Recorded, AI summary

Vulnerability prioritization is hard. Severity tells you how serious a flaw is, the Exploit Prediction Scoring System (EPSS) indicates how likely it is to be exploited, and runtime context shows what's actually running. Reachability adds application-specific context by showing whether your code can call the vulnerable function.
In this session, you'll learn how to use reachability to make more informed prioritization decisions. A live demo will show function-level reachability directly in Dependabot, including the evidence behind the result and how teams may use that information when prioritizing alerts. You'll leave with a practical framework for focusing remediation efforts where they matter most.

**Speakers**

- Carlin Cherry: Senior Product Manager, GitHub
- Ankit Kumar Honey: Senior Engineering Manager, GitHub

```json
{"day": "2026-10-28", "start": "15:10", "end": "15:25",
 "title": "How to think about reachability and use it to prioritize vulnerabilities", "room": "Silent Disco Demos",
 "speaker": "Carlin Cherry (GitHub), Ankit Kumar Honey (GitHub)",
 "note": "You'll learn how to use reachability to make more informed prioritization decisions."}
```

### 3:15 PM

#### Session After Party: Disrupting supply chain attacks: A threat framework for GitHub Actions

**Wednesday, Oct 28 · 3:15 PM - 3:45 PM PDT**  
**Where:** The Speakeasy @ GitHub Central, Festival Pavilion  
**Type:** Session After Party · **Format:** In-person

This is an informal follow-up Q&A to the main stage session "Disrupting supply chain attacks: A threat framework for GitHub Actions." Right after the talk, join Greg Ose and Steve Glass in GitHub Central. Bring your questions and keep the conversation going.

**Speakers**

- Steve Glass: Senior Product Manager, GitHub
- Greg Ose: Principal Product Security Engineer, GitHub

```json
{"day": "2026-10-28", "start": "15:15", "end": "15:45",
 "title": "Session After Party: Disrupting supply chain attacks: A threat framework for GitHub Actions", "room": "The Speakeasy (GitHub Central)",
 "speaker": "Steve Glass (GitHub), Greg Ose (GitHub)",
 "note": "This is an informal follow-up Q&A to the main stage session \"Disrupting supply chain attacks: A threat framework for GitHub Actions.\"..."}
```

### 3:20 PM

#### Beyond the prompt: Building an AI that takes initiative

**Wednesday, Oct 28 · 3:20 PM - 3:50 PM PDT**  
**Where:** Main Stage @ Festival Pavilion  
**Type:** Main Stage · **Format:** In-person, Recorded, AI summary

Cameron Hamilton asked his AI assistant, HALIE, to connect the camera in his son's nursery. It turned that camera into a baby monitor he never asked for. When he asked it to automate business growth, it told him to meet customers in person. And when he audited its work, 38 of its 96 goals were about improving itself. How do you make a proactive agent dependable? This session walks through HALIE's three systems: anticipation (acting on needs without a prompt), self-evolution (improving its own tools and code), and metacognition (reviewing work and conversations to steer what comes next). Cameron covers experiments in making useful initiative repeatable, the architecture behind it, what it costs to run an agent on cheap models, and which decisions still need a human. You'll leave with practical ways to design agents that decide what to do next, learn from what helped, and earn more responsibility through measurable results.

**Speakers**

- Cameron Hamilton: Creator, Alliance AI

```json
{"day": "2026-10-28", "start": "15:20", "end": "15:50",
 "title": "Beyond the prompt: Building an AI that takes initiative", "room": "Main Stage",
 "speaker": "Cameron Hamilton (Alliance AI)",
 "note": "This session walks through HALIE's three systems: anticipation (acting on needs without a prompt), self-evolution (improving its own..."}
```

### 3:25 PM

#### Rediscover the command line: Practical workflows with GitHub CLI

**Wednesday, Oct 28 · 3:25 PM - 3:40 PM PDT**  
**Where:** Demos & Donuts @ Gateway Pavilion, Level 2  
**Type:** Product Demo · **Format:** In-person, AI summary

Are you using the command line to its full potential? In this session, Ryan Hecht and Ayman Bagabas start with fundamentals like Unix pipes and shell scripts, and builds up to real workflows using GitHub CLI, Git, Gum, and GitHub Copilot CLI. 

Showing how each tool connects into workflows you can take back to your terminal immediately, this demo is full of real scripts solving real problems. You'll leave with a stronger command line foundation and concrete workflows that make you faster, whether you're a CLI skeptic or already live in the terminal.

**Speakers**

- Ryan Hecht: Product Manager, GitHub
- Ayman Bagabas: Senior Software Engineer, GitHub

```json
{"day": "2026-10-28", "start": "15:25", "end": "15:40",
 "title": "Rediscover the command line: Practical workflows with GitHub CLI", "room": "Demos & Donuts (Level 2)",
 "speaker": "Ryan Hecht (GitHub), Ayman Bagabas (GitHub)",
 "note": "Ryan Hecht and Ayman Bagabas start with fundamentals like Unix pipes and shell scripts, and builds up to real workflows using GitHub..."}
```

### 3:30 PM

#### Stop guessing: What 100M pull requests and 150T tokens tell us about AI impact (Sponsored)

**Wednesday, Oct 28 · 3:30 PM - 3:45 PM PDT**  
**Where:** Silent Disco Demos @ Festival Pavilion  
**Type:** Product Demo · **Format:** In-person, Recorded, AI summary

A year ago, the question was: Is GitHub Copilot working? Now there are answers. Jellyfish's analysis of 100+ million pull requests, 90+ million prompts, and 150+ trillion tokens from more than 275K software engineers reveals what high-performing teams do differently with AI coding—and why so many companies still struggle to scale its value.

Adam Ferrari, SVP of Engineering at Jellyfish, shares the data and shows how to separate broad-but-shallow adoption from the patterns that actually move productivity, throughput, and team effectiveness. You'll leave knowing which signals to watch, what distinguishes mature AI programs from surface-level rollouts, and how to connect Copilot activity to metrics your business cares about.

**Speakers**

- Adam Ferrari: SVP of Engineering, Jellyfish

```json
{"day": "2026-10-28", "start": "15:30", "end": "15:45",
 "title": "Stop guessing: What 100M pull requests and 150T tokens tell us about AI impact (Sponsored)", "room": "Silent Disco Demos",
 "speaker": "Adam Ferrari (Jellyfish)",
 "note": "You'll leave knowing which signals to watch, what distinguishes mature AI programs from surface-level rollouts, and how to connect..."}
```

#### How to see what your agent is building before it builds it (Sponsored)

**Wednesday, Oct 28 · 3:30 PM - 4:10 PM PDT**  
**Where:** Cowell Theater @ Gateway Pavilion  
**Type:** Breakout Session · **Format:** In-person, AI summary

Your agent is shipping code faster than your team can follow. But there's one problem: nobody can see what's being built before it happens. 

In this session, Jake Albaugh demos a workflow that connects Figma and GitHub Copilot through MCP, showing you how to turn your codebase into a visual plan on a FigJam canvas, get team alignment, and feed that context directly into the GitHub Copilot cloud agent. 

You'll see the full loop live and leave with a repeatable workflow that plugs into your existing GitHub and Figma setup.

**Speakers**

- Jake Albaugh: Developer Advocate, Figma

```json
{"day": "2026-10-28", "start": "15:30", "end": "16:10",
 "title": "How to see what your agent is building before it builds it (Sponsored)", "room": "Cowell Theater",
 "speaker": "Jake Albaugh (Figma)",
 "note": "Jake Albaugh demos a workflow that connects Figma and GitHub Copilot through MCP, showing you how to turn your codebase into a visual..."}
```

#### PATs, rulesets, and IP allowlists: How Confluent secured GitHub Enterprise Cloud

**Wednesday, Oct 28 · 3:30 PM - 4:10 PM PDT**  
**Where:** Silent Disco Breakouts @ Festival Pavilion  
**Type:** Breakout Session · **Format:** In-person, AI summary

Securing a GitHub Enterprise organization can be an intimidating exercise, especially at scale. In this session, Confluent shares hard-won lessons from rolling out security controls across their organization: what worked, what backfired, and the gaps they didn't see coming. They'll start with the basics, then get into the messy details: managing repos with infrastructure as code, choosing between branch protection and rulesets, migrating from personal access tokens (PATs) to GitHub Apps, rolling out IP allowlists, and more. You'll leave with a practical roadmap for maturing your own GitHub organization's security posture, and a clearer sense of which controls are worth the effort.

**Speakers**

- Luke Young: Principal Security Engineer, Confluent

```json
{"day": "2026-10-28", "start": "15:30", "end": "16:10",
 "title": "PATs, rulesets, and IP allowlists: How Confluent secured GitHub Enterprise Cloud", "room": "Silent Disco Breakouts",
 "speaker": "Luke Young (Confluent)",
 "note": "Confluent shares hard-won lessons from rolling out security controls across their organization: what worked, what backfired, and the..."}
```

#### Still open: How AI reshaped open source

**Wednesday, Oct 28 · 3:30 PM - 4:10 PM PDT**  
**Where:** BATS Theatre @ Fort Mason Building B, 3rd Floor  
**Type:** Panel Discussion · **Format:** In-person, AI summary

Open source isn't dying. It's being stress-tested in ways nobody anticipated. AI has accelerated contributions and made it easier than ever to ship code, but it's also introduced new questions about quality, governance, and what community means when bots can contribute at machine scale. 

In this session, three leaders from the open source foundations community share what they're actually seeing: why AI makes open source more essential than ever, what maintainers are doing right now to handle the surge in AI-assisted contributions, and how foundations are updating governance structures that were built for human contributors. You'll leave with a clear picture of where open source stands today and what needs to change.

**Speakers**

- Ashley Wolf: Director, Open Source Programs, GitHub
- David A. Wheeler: Fellow/Director of Open Source Supply Chain Security, OpenSSF, The Linux Foundation
- Angie Jones: VP, Agentic AI Foundation
- Priya Pahwa: Director, Django Software Foundation

```json
{"day": "2026-10-28", "start": "15:30", "end": "16:10",
 "title": "Still open: How AI reshaped open source", "room": "BATS Theatre, 3rd Floor",
 "speaker": "Ashley Wolf (GitHub), David A. Wheeler (The Linux Foundation), Angie Jones (Agentic AI Foundation), Priya Pahwa (Django Software Foundation)",
 "note": "Three leaders from the open source foundations community share what they're actually seeing: why AI makes open source more essential..."}
```

#### GitHub Copilot at scale: An interactive lab for enterprise admins

**Wednesday, Oct 28 · 3:30 PM - 4:15 PM PDT**  
**Where:** Sandbox @ Fort Mason Building C, Founders Inc., 3rd Floor  
**Type:** Sandbox Session · **Format:** In-person

Rolling out GitHub Copilot across an enterprise takes more than assigning seats. In this interactive lab run by technical staff, you’ll configure a sample rollout and work through the settings that shape how teams use Copilot. 

We’ll explore utilization-based billing tools, API options, common configuration issues, and the decisions that matter when moving from a pilot to a wider rollout. Bring your questions and leave with a better understanding of Copilot’s enterprise controls, plus a checklist you can adapt to your organization.

**Speakers**

- David Losert: Strategic Technical Architect, International, GitHub
- April Yoho: Senior Developer Advocate, GitHub

```json
{"day": "2026-10-28", "start": "15:30", "end": "16:15",
 "title": "GitHub Copilot at scale: An interactive lab for enterprise admins", "room": "Sandbox, 3rd Floor",
 "speaker": "David Losert (GitHub), April Yoho (GitHub)",
 "note": "Rolling out GitHub Copilot across an enterprise takes more than assigning seats."}
```

#### What happens between pressing Enter and getting a response from GitHub Copilot

**Wednesday, Oct 28 · 3:30 PM - 5:00 PM PDT**  
**Where:** Workshops @ Gateway Pavilion, Level 1  
**Type:** Workshop · **Format:** In-person

What are AI credits, and why does typing a few words consume thousands of them? Every GitHub Copilot interaction assembles a layered prompt before anything reaches the model. Most developers never see this process, which makes slow or irrelevant responses hard to diagnose. 

In this session, Ken Muse and Mickey Gousset open up the pipeline: how VS Code builds these prompts, how the prioritization engine decides what stays in the context window and what gets silently dropped, and what real-world patterns look like in the debug logs. You'll leave knowing how to engineer your interactions for maximum signal and minimum waste.

**Speakers**

- Ken Muse: Staff DevOps Architect | ODST | FDE, GitHub
- Mickey Gousset: Staff DevOps Architect | ODST | FDE, GitHub

```json
{"day": "2026-10-28", "start": "15:30", "end": "17:00",
 "title": "What happens between pressing Enter and getting a response from GitHub Copilot", "room": "Workshops (Level 1)",
 "speaker": "Ken Muse (GitHub), Mickey Gousset (GitHub)",
 "note": "Ken Muse and Mickey Gousset open up the pipeline: how VS Code builds these prompts, how the prioritization engine decides what stays in..."}
```

### 3:40 PM

#### Building Copilot in the cloud

**Wednesday, Oct 28 · 3:40 PM - 3:55 PM PDT**  
**Where:** Ship & Tell @ Firehouse  
**Type:** Ship & Tell · **Format:** In-person, Recorded, AI summary

Copilot is great at helping developers write code on their machines, but running agents in the cloud is a major step up in productivity. Making that work takes an experience developers can trust, backed by a safe place to run, the right access to repositories and tools, and enough compute to get the job done. This session goes behind the scenes at how product and platform come together to make cloud agents work, from delegation and review to isolated sandboxes, orchestration, identity, and permissions. You'll leave understanding what it takes to run cloud agents safely, and why you can trust these agents to handle the real work.

**Speakers**

- Jason Etcovitch: Principal Software Engineer, GitHub
- Matt Alvarez: Principal Software Engineer, GitHub

```json
{"day": "2026-10-28", "start": "15:40", "end": "15:55",
 "title": "Building Copilot in the cloud", "room": "Ship & Tell",
 "speaker": "Jason Etcovitch (GitHub), Matt Alvarez (GitHub)",
 "note": "This session goes behind the scenes at how product and platform come together to make cloud agents work, from delegation and review to..."}
```

### 3:45 PM

#### Agentic modernization of .NET and Java apps with GitHub Copilot

**Wednesday, Oct 28 · 3:45 PM - 4:00 PM PDT**  
**Where:** Demos & Donuts @ Gateway Pavilion, Level 2  
**Type:** Product Demo · **Format:** In-person, AI summary

Legacy app modernization shouldn't start with a blank repo and a risky rewrite. This session shows how GitHub Copilot app modernization — GitHub's AI-powered toolset for upgrading and migrating legacy applications — helps teams analyze, plan, refactor, test, secure, and migrate .NET and Java apps across IDE and CLI workflows.

You'll see a practical modernization playbook that combines GitHub Copilot app modernization, GitHub Actions, built-in security checks, and Azure-ready migration patterns. This turns a traditionally slow, high-risk effort into one that's safer, faster, and repeatable at scale. Rather than rewriting from scratch, teams assess what they have, upgrade frameworks and dependencies, remediate vulnerabilities, validate with tests, and move to the cloud with a human in the loop at each step.

**Speakers**

- Kaush Ganguly: Sr. Cloud Solution Architect - AI Apps, Microsoft

```json
{"day": "2026-10-28", "start": "15:45", "end": "16:00",
 "title": "Agentic modernization of .NET and Java apps with GitHub Copilot", "room": "Demos & Donuts (Level 2)",
 "speaker": "Kaush Ganguly (Microsoft)",
 "note": "This session shows how GitHub Copilot app modernization - GitHub's AI-powered toolset for upgrading and migrating legacy applications ..."}
```

### 3:50 PM

#### From x86/x64 to Arm: Migrating a Large-Scale Linux Web App with GitHub Copilot (Sponsored)

**Wednesday, Oct 28 · 3:50 PM - 4:05 PM PDT**  
**Where:** Silent Disco Demos @ Festival Pavilion  
**Type:** Product Demo · **Format:** In-person, Recorded, AI summary

As software development becomes increasingly agentic, the infrastructure those agents run on matters. In this session, you’ll see GitHub Copilot use the Arm MCP server and multiple Cobalt 200 cloud VMs as Arm-native secondary compute for a real migration workflow: moving an existing x86/x64 Linux web application onto a 100% Arm-native path – from development and builds through GitHub Actions and deployment. Once the app is running, we'll use Arm Performix to pinpoint and fix performance bottlenecks, then validate each optimization with data from the live workload. You’ll leave with three ways to judge the workflow – task success, task time, and cost per successful task – and a clearer sense of how Arm native compute and continuous performance validation fit into agentic development.

**Speakers**

- Michael Gamble: partner marketing, Arm

```json
{"day": "2026-10-28", "start": "15:50", "end": "16:05",
 "title": "From x86/x64 to Arm: Migrating a Large-Scale Linux Web App with GitHub Copilot (Sponsored)", "room": "Silent Disco Demos",
 "speaker": "Michael Gamble (Arm)",
 "note": "You'll see GitHub Copilot use the Arm MCP server and multiple Cobalt 200 cloud VMs as Arm-native secondary compute for a real migration..."}
```

### 4:00 PM

#### Women in Tech Networking Reception

**Wednesday, Oct 28 · 4:00 PM - 5:00 PM PDT**  
**Where:** Outdoor Theater @ Gateway Plaza  
**Type:** Social

Join us for an exclusive gathering designed for industry trailblazers across our customer, partner, and Hubber communities. Connect with fellow leaders, spark high-impact mentor connections, and expand your network over hand-crafted cocktails, mocktails, and light bites.

Attendees will also take home exclusive Women in Tech swag created specially for GitHub Universe.

```json
{"day": "2026-10-28", "start": "16:00", "end": "17:00",
 "title": "Women in Tech Networking Reception", "room": "Outdoor Theater",
 "speaker": "",
 "note": "Join us for an exclusive gathering designed for industry trailblazers across our customer, partner, and Hubber communities."}
```

### 4:05 PM

#### What Copilot code review catches (and how to build a custom agent for the rest)

**Wednesday, Oct 28 · 4:05 PM - 4:20 PM PDT**  
**Where:** Demos & Donuts @ Gateway Pavilion, Level 2  
**Type:** Product Demo · **Format:** In-person, AI summary

Teams are merging more pull requests per day, and senior engineers can't review them all. 

In this session, David Pereira does a live walkthrough of what Copilot code review handles out of the box, then builds a custom agent using the Copilot SDK with focused sub-agents for concerns like performance and architecture. You'll learn how to pair built-in review with custom agents that enforce your team's specific standards, along with practical patterns for building reliable agents with the SDK.

**Speakers**

- David Pereira: AI & Digital Solution Architect, Siemens Energy

```json
{"day": "2026-10-28", "start": "16:05", "end": "16:20",
 "title": "What Copilot code review catches (and how to build a custom agent for the rest)", "room": "Demos & Donuts (Level 2)",
 "speaker": "David Pereira (Siemens Energy)",
 "note": "David Pereira does a live walkthrough of what Copilot code review handles out of the box, then builds a custom agent using the Copilot..."}
```

#### Session After Party: Beyond the prompt: Building an AI that takes initiative

**Wednesday, Oct 28 · 4:05 PM - 4:35 PM PDT**  
**Where:** The Speakeasy @ GitHub Central, Festival Pavilion  
**Type:** Session After Party · **Format:** In-person

This is an informal follow-up Q&A to the main stage session "Beyond the prompt: Building an AI that takes initiative." Right after the talk, join Cameron Hamilton (Alliance AI) in GitHub Central. Bring your questions and keep the conversation going.

**Speakers**

- Cameron Hamilton: Creator, Alliance AI

```json
{"day": "2026-10-28", "start": "16:05", "end": "16:35",
 "title": "Session After Party: Beyond the prompt: Building an AI that takes initiative", "room": "The Speakeasy (GitHub Central)",
 "speaker": "Cameron Hamilton (Alliance AI)",
 "note": "This is an informal follow-up Q&A to the main stage session \"Beyond the prompt: Building an AI that takes initiative.\" Right after the..."}
```

### 4:10 PM

#### How a shared AI config became Slack's internal tool platform

**Wednesday, Oct 28 · 4:10 PM - 4:25 PM PDT**  
**Where:** Ship & Tell @ Firehouse  
**Type:** Ship & Tell · **Format:** In-person, Recorded, AI summary

Frances Coronel, a product engineer at Slack, built a personal AI setup to work faster and shared it in a public channel. Engineers across the company started forking it without being asked. That organic pull grew into Slack's internal AI tool catalog: a single source of truth for MCP servers, skills, and agents, backed by an adoption dashboard tracking real usage data across teams. 

In this session, Frances demos the catalog, shares six months of real adoption metrics, and shows how a personal productivity hack became org-wide infrastructure. You'll learn how to build an internal AI tool catalog on GitHub, measure adoption with real data instead of surveys, and create the cultural conditions that make AI tooling spread on its own.

**Speakers**

- Frances Coronel: Senior Software Engineer, Slack

```json
{"day": "2026-10-28", "start": "16:10", "end": "16:25",
 "title": "How a shared AI config became Slack's internal tool platform", "room": "Ship & Tell",
 "speaker": "Frances Coronel (Slack)",
 "note": "Frances demos the catalog, shares six months of real adoption metrics, and shows how a personal productivity hack became org-wide..."}
```

#### One skill, one CLI, one production health report

**Wednesday, Oct 28 · 4:10 PM - 4:25 PM PDT**  
**Where:** Silent Disco Demos @ Festival Pavilion  
**Type:** Product Demo · **Format:** In-person, Recorded, AI summary

It started as an idea: could Copilot CLI generate a real health report for a database fleet? Xin Wu wrote a single skill, hit a wall, and spent weeks working with the agent until it provided a trustworthy report. 

In this Ship & Tell, Xin shares the journey from first skill to a report accurate enough to actually ship, including how to review AI-generated output without redoing all the work.

**Speakers**

- Xin Wu: Principal Software Engineer, GitHub

```json
{"day": "2026-10-28", "start": "16:10", "end": "16:25",
 "title": "One skill, one CLI, one production health report", "room": "Silent Disco Demos",
 "speaker": "Xin Wu (GitHub)",
 "note": "It started as an idea: could Copilot CLI generate a real health report for a database fleet?"}
```

#### Build without breaking trust (Sponsored)

**Wednesday, Oct 28 · 4:10 PM - 4:40 PM PDT**  
**Where:** Main Stage @ Festival Pavilion  
**Type:** Main Stage · **Format:** In-person, Recorded, AI summary

AI can help a business team get to a working solution quickly. The more challenging test is whether that solution fits into the rest of the stack. In an Avanade project for a manufacturing customer, Forward Deployed Engineers (FDEs) rebuilt a business process with the team and proved the technology worked. But the build was designed around that one process, without accounting for core systems, adjacent workflows, or the handoffs between them—so it didn't scale. 

In this session, you’ll see an anonymized before-and-after architecture diagram showing how the team changed its approach by pairing FDEs with a Trust Architect. You’ll learn why a successful proof of concept can still be hard to integrate, what each role owns, and how to assign ownership where low-code work hands off to pro-code engineering.

**Speakers**

- Aaron Reich: Chief Technology Officer, Avanade

```json
{"day": "2026-10-28", "start": "16:10", "end": "16:40",
 "title": "Build without breaking trust (Sponsored)", "room": "Main Stage",
 "speaker": "Aaron Reich (Avanade)",
 "note": "You'll see an anonymized before-and-after architecture diagram showing how the team changed its approach by pairing FDEs with a Trust..."}
```

### 4:25 PM

#### When is local Copilot worth it? Three open-weight coders vs. Copilot out of the box

**Wednesday, Oct 28 · 4:25 PM - 4:40 PM PDT**  
**Where:** Demos & Donuts @ Gateway Pavilion, Level 2  
**Type:** Product Demo · **Format:** In-person, AI summary

Bring your own key (BYOK) for GitHub Copilot is now generally available, and open-weight coding models keep landing on Hugging Face every few weeks. But BYOK doesn't cover code completions, embeddings, or repository indexing. So when does running a local model actually pay off? 

Alpha Romer Coma is benchmarking three open-weight coders on a single RTX 4090 and an Apple M5 chip against GitHub Copilot's default agent mode on real repository tasks, reporting time to first token, tool-call accuracy, and task completion rate. In this session, you'll see which workload patterns on real tasks favor a local GPU, which favor Copilot out of the box, and you'll learn how to run the same comparison on your own repositories.

**Speakers**

- Alpha Romer Coma: Senior Data Engineer, ViableView

```json
{"day": "2026-10-28", "start": "16:25", "end": "16:40",
 "title": "When is local Copilot worth it? Three open-weight coders vs. Copilot out of the box", "room": "Demos & Donuts (Level 2)",
 "speaker": "Alpha Romer Coma (ViableView)",
 "note": "You'll see which workload patterns on real tasks favor a local GPU, which favor Copilot out of the box, and you'll learn how to run the..."}
```

### 4:30 PM

#### Connecting Copilot

**Wednesday, Oct 28 · 4:30 PM - 4:45 PM PDT**  
**Where:** Silent Disco Demos @ Festival Pavilion  
**Type:** Product Demo · **Format:** In-person, Recorded, AI summary

Extending and customizing GitHub Copilot is now easier than ever! 
 
In this session you'll learn how to discover exactly what agent skills, plugins, and MCP servers you need via a powerful, new AI agent resource search. You'll also see how to setup once and run your connections everywhere. These new features are easy to use and help you avoid manually managing JSON configuration. 
 
Whether you use the GitHub Copilot app, Copilot CLI, VS Code, or Copilot in github.com, you can discover, authorize once, and instantly use your favorite services like Sentry, Cloudflare, Notion, Microsoft 365, Azure, Figma, and more, anywhere you use Copilot. And on shared workstations, signing out of Copilot automatically revokes access to your connected services. 
 
Join us for a first look at a simpler way to connect Copilot to the tools you rely on.

**Speakers**

- Sam Morrow: Staff Software Engineer, GitHub

```json
{"day": "2026-10-28", "start": "16:30", "end": "16:45",
 "title": "Connecting Copilot", "room": "Silent Disco Demos",
 "speaker": "Sam Morrow (GitHub)",
 "note": "Plugins, and MCP servers you need via a powerful, new AI agent resource search."}
```

#### Security by default: a maintainer’s wishlist for GitHub Actions v2

**Wednesday, Oct 28 · 4:30 PM - 5:10 PM PDT**  
**Where:** Cowell Theater @ Gateway Pavilion  
**Type:** Breakout Session · **Format:** In-person, AI summary

GitHub Actions has a reputation for insecure defaults. This session takes that reputation seriously and covers questions that follow from it. First, in 2026, how are teams closing the gap between the platform's defaults and the security posture they actually want? And second, how can GitHub ship the security features that make Actions the default choice for the next decade without losing the openness that makes it accessible to contributors and newcomers?

Along the way, you'll get a fast tour of Actions' best-known footguns and their fixes, a look at how attacker behavior has shifted over the past year, and an honest picture of what a security-by-default "v2" of GitHub Actions could look like.

**Speakers**

- William Woodruff: Member of Technical Staff, OpenAI

```json
{"day": "2026-10-28", "start": "16:30", "end": "17:10",
 "title": "Security by default: a maintainer's wishlist for GitHub Actions v2", "room": "Cowell Theater",
 "speaker": "William Woodruff (OpenAI)",
 "note": "This session takes that reputation seriously and covers questions that follow from it."}
```

#### The human side of AI: How building community drove 94% Copilot adoption

**Wednesday, Oct 28 · 4:30 PM - 5:10 PM PDT**  
**Where:** BATS Theatre @ Fort Mason Building B, 3rd Floor  
**Type:** Breakout Session · **Format:** In-person, AI summary

What if scaling AI isn’t about better models, but better human connection? Learn how a large U.S.-based financial services firm achieved 94% GitHub Copilot adoption and 78% agent-written code by combining grassroots engagement, storytelling, and innersource, making AI something developers wanted to use and build together. This session shares how treating AI adoption as a people challenge drives trust, plus how to measure meaningful adoption through impact.

**Speakers**

- Brittany Istenes: OSS strategist/Community Architect, Independent

```json
{"day": "2026-10-28", "start": "16:30", "end": "17:10",
 "title": "The human side of AI: How building community drove 94% Copilot adoption", "room": "BATS Theatre, 3rd Floor",
 "speaker": "Brittany Istenes (Independent)",
 "note": "Learn how a large U.S.-based financial services firm achieved 94% GitHub Copilot adoption and 78% agent-written code by combining..."}
```

#### What happens behind the scenes when you run npm install

**Wednesday, Oct 28 · 4:30 PM - 5:10 PM PDT**  
**Where:** Silent Disco Breakouts @ Festival Pavilion  
**Type:** Breakout Session · **Format:** In-person, AI summary

Every npm install pulls in code from a sprawling network of packages, maintainers, and automation you've never met and mostly can't see. So what are you actually trusting when you run it?

This talk traces a single npm install down to what it really depends on: who can publish a package, what stops them from shipping something malicious, and where those safeguards break. You'll see how recent attacks slipped through, what npm audit does and doesn't catch, and how provenance and OpenID Connect (OIDC) now let you verify that a package was built by who it claims.

You'll leave with a mental model for reading the risk in your own dependency tree, and a few concrete checks to run before you trust the next package you pull in.

**Speakers**

- Karen Li: Software Engineer III, GitHub
- Leo Balter: Senior Product Manager, GitHub

```json
{"day": "2026-10-28", "start": "16:30", "end": "17:10",
 "title": "What happens behind the scenes when you run npm install", "room": "Silent Disco Breakouts",
 "speaker": "Karen Li (GitHub), Leo Balter (GitHub)",
 "note": "This talk traces a single npm install down to what it really depends on: who can publish a package, what stops them from shipping..."}
```

### 4:40 PM

#### What open source can teach us about agents in CI/CD

**Wednesday, Oct 28 · 4:40 PM - 4:55 PM PDT**  
**Where:** Ship & Tell @ Firehouse  
**Type:** Ship & Tell · **Format:** In-person, Recorded, AI summary

What happens when you build an operating system the way you build an application? Jorge Castro uses projectbluefin.io to show how container images, CI/CD, GitOps, and open source projects can work together in a reproducible software supply chain. 

The session starts with a pipeline that builds and publishes a containerized operating system. From there, Jorge shows where agents can help: generating or updating configuration, responding to changes in the pipeline, and working with the tools that build and deliver the system. He’ll also cover the limits of this approach, including how teams keep changes reviewable, traceable, and safe to reproduce. 

You’ll leave with a concrete pattern for adding agents to an existing CI/CD workflow without treating AI as a replacement for the pipeline, its controls, or the people reviewing its changes.

**Speakers**

- Jorge Castro: Open Source Community Engineer and Developer Relations, CNCF

```json
{"day": "2026-10-28", "start": "16:40", "end": "16:55",
 "title": "What open source can teach us about agents in CI/CD", "room": "Ship & Tell",
 "speaker": "Jorge Castro (CNCF)",
 "note": "The session starts with a pipeline that builds and publishes a containerized operating system."}
```

### 4:45 PM

#### Agentic Workflows: Automation at scale

**Wednesday, Oct 28 · 4:45 PM - 5:15 PM PDT**  
**Where:** The Speakeasy @ GitHub Central, Festival Pavilion  
**Type:** Breakout Session · **Format:** In-person, AI summary

Automation is how we buy time for craft, enforce correctness in situations that require judgment, and improve our software at business scale. Learn how to start automating, as well as how you can start to setup your software factory with governance, monitoring, and security so you can roll out automations to everyone in your business!

**Speakers**

- Landon Cox: Senior Principle Researcher, Microsoft
- Peli de Halleux: Agentic Engineer, GitHub Next, Microsoft

```json
{"day": "2026-10-28", "start": "16:45", "end": "17:15",
 "title": "Agentic Workflows: Automation at scale", "room": "The Speakeasy (GitHub Central)",
 "speaker": "Landon Cox (Microsoft), Peli de Halleux (Microsoft)",
 "note": "Learn how to start automating, as well as how you can start to setup your software factory with governance, monitoring, and security so..."}
```

#### Goodbye, tutorial hell: AI guides and the new documentation layer

**Wednesday, Oct 28 · 4:45 PM - 5:30 PM PDT**  
**Where:** Sandbox @ Fort Mason Building C, Founders Inc., 3rd Floor  
**Type:** Sandbox Session · **Format:** In-person

For years, "developer education" has meant read the docs and hope. And most MCP servers are just API wrappers with extra steps. What if the server could teach instead? 

When an AI agent in GitHub Copilot or another MCP-compatible editor reads documentation through an opinionated MCP server, it stops giving generic advice and starts teaching the way your product is meant to be used. 

Claire Waters and Erin Mikail Staples show the difference live: you'll fork an open source reference server, install it in your editor, and watch agent behavior change side by side. You'll leave with a working scaffold you can adapt for your own product or codebase.

**Speakers**

- Erin Mikail Staples: Staff Developer Experience Engineer, Tiger Data
- Janice Niemeir: Director, Docs Engagement & Experience, GitHub

```json
{"day": "2026-10-28", "start": "16:45", "end": "17:30",
 "title": "Goodbye, tutorial hell: AI guides and the new documentation layer", "room": "Sandbox, 3rd Floor",
 "speaker": "Erin Mikail Staples (Tiger Data), Janice Niemeir (GitHub)",
 "note": "You'll leave with a working scaffold you can adapt for your own product or codebase."}
```

### 5:00 PM

#### Beyond the code: How Forge powers the rest of the SDLC

**Wednesday, Oct 28 · 5:00 PM - 5:15 PM PDT**  
**Where:** Ship & Tell @ Firehouse  
**Type:** Ship & Tell · **Format:** In-person, Recorded, AI summary

GitHub Copilot changed how developers at Micron write code, but the team saw a larger opportunity in applying AI across the entire software development lifecycle. Engineering teams went all-in on Copilot, leveraging its full capabilities and partnering closely with Microsoft to help shape new features based on real-world enterprise needs. 

This session introduces Forge, an AI-powered engineering platform that drives measurable gains in productivity, quality, and speed by extending Copilot beyond coding to enable agentic workflows across planning, development, testing, documentation, and delivery. You’ll see exactly how one shared platform can replace duplicate, team-by-team agent efforts, along with how to treat context as shared infrastructure for agentic work.

**Speakers**

- Kevin Kennedy: Principal Software Engineer, Micron Technology
- Josh McIntosh: Senior Software Development Manager, Micron Technology Inc.

```json
{"day": "2026-10-28", "start": "17:00", "end": "17:15",
 "title": "Beyond the code: How Forge powers the rest of the SDLC", "room": "Ship & Tell",
 "speaker": "Kevin Kennedy (Micron Technology), Josh McIntosh (Micron Technology Inc.)",
 "note": "This session introduces Forge, an AI-powered engineering platform that drives measurable gains in productivity, quality, and speed by..."}
```

#### Sunset Boat Cruise

**Wednesday, Oct 28 · 5:00 PM - 7:00 PM PDT**  
**Where:** Pier 43 1/2 @ Fisherman's Wharf  
**Type:** Social

Sonar and Factory are heading to San Francisco for GitHub Universe — and we're making the most of it. On Wednesday, October 28, we're hosting a sunset cruise on the Bay from 5–7pm. Think golden hour views, good drinks, and great conversations with people who care about building better software. You don't need to be attending Universe to join us — the cruise is open to everyone. But space is limited, so grab your spot before it fills up.

Hosted by Sonar & Factory. Advance registration required.

```json
{"day": "2026-10-28", "start": "17:00", "end": "19:00",
 "title": "Sunset Boat Cruise", "room": "Pier 43 1/2",
 "speaker": "",
 "note": "Sonar and Factory are heading to San Francisco for GitHub Universe - and we're making the most of it."}
```

#### Ship It Afterparty

**Wednesday, Oct 28 · 5:00 PM - 8:00 PM PDT**  
**Where:** Left Door @ 1905 Union St  
**Type:** Social

Your agent can build the change. You have to decide whether it deserves to ship. Join Amplitude and Statsig for a GitHub Universe afterparty built for builders. Race through a fast-paced AI product challenge, make the call, and see whether your decisions survive the data.

Hosted by Amplitude. Advance registration required .

```json
{"day": "2026-10-28", "start": "17:00", "end": "20:00",
 "title": "Ship It Afterparty", "room": "Left Door",
 "speaker": "",
 "note": "Join Amplitude and Statsig for a GitHub Universe afterparty built for builders."}
```

### 5:30 PM

#### AI in Motion: New Trajectories Evening Reception

**Wednesday, Oct 28 · 5:30 PM - 7:30 PM PDT**  
**Where:** Culinary Artistas @ 851 Beach St  
**Type:** Social

Join Slalom for an evening of connection, conversation, and out-of-this-world perspectives, co-sponsored by Moderne.io and Microsoft. As organizations move beyond experimentation and bring AI into enterprise-wide orbit, the focus is shifting from what’s possible to what’s next. This gathering brings together technology leaders, developers, and innovators to explore how leading organizations are gaining momentum, accelerating innovation, and charting a course from AI investment to measurable business impact. Connect with peers navigating similar opportunities and challenges, exchange ideas and experiences, and explore the new frontiers shaping an AI-powered future.

Hosted by Slalom. Advance registration required .

```json
{"day": "2026-10-28", "start": "17:30", "end": "19:30",
 "title": "AI in Motion: New Trajectories Evening Reception", "room": "Culinary Artistas",
 "speaker": "",
 "note": "Join Slalom for an evening of connection, conversation, and out-of-this-world perspectives, co-sponsored by Moderne.io and Microsoft."}
```

#### Happy hour hosted by Faros

**Wednesday, Oct 28 · 5:30 PM - 7:30 PM PDT**  
**Where:** Radhaus @ Fort Mason  
**Type:** Social

No need to go far. The after party is just steps from your last session. Join Faros after Day 1 of GitHub Universe for an on-campus happy hour designed to keep the day’s “tokenomics” conversations going in a more relaxed setting. Connect with fellow engineering and technology leaders, exchange perspectives, and reflect on the ideas shaping the future.

Hosted by Faros. Advance registration required .

```json
{"day": "2026-10-28", "start": "17:30", "end": "19:30",
 "title": "Happy hour hosted by Faros", "room": "Radhaus",
 "speaker": "",
 "note": "Join Faros after Day 1 of GitHub Universe for an on-campus happy hour designed to keep the day's \"tokenomics\" conversations going in a..."}
```

#### NeuBird + FluidCloud Happy Hour

**Wednesday, Oct 28 · 5:30 PM - 7:30 PM PDT**  
**Where:** For the Record @ 2120 Greenwich St  
**Type:** Social

Join NeuBird and FluidCloud for an exclusive happy hour following GitHub Universe! Connect with fellow developers, engineering leaders, and industry peers over drinks, bites, and great conversation at For The Record in San Francisco. Space is limited, so request your spot to join us!

Hosted by NeuBird and FluidCloud. Advance registration required .

```json
{"day": "2026-10-28", "start": "17:30", "end": "19:30",
 "title": "NeuBird + FluidCloud Happy Hour", "room": "For the Record",
 "speaker": "",
 "note": "Join NeuBird and FluidCloud for an exclusive happy hour following GitHub Universe!"}
```

#### Recovery Hour with Rubrik

**Wednesday, Oct 28 · 5:30 PM - 8:30 PM PDT**  
**Where:** Barrio @ 900 North Point St  
**Type:** Social

Join Rubrik at Barrio for drinks, bites, and the kind of hallway conversations that never fit in a session slot. No slides. No pitch. No merge conflicts. Just good people who know the best systems — and the best evenings — are the ones you can always get back. What to expect: - Drinks named after the commands you fear most — yes, there's a Force Push, and no, it won't overwrite anything. - Barrio's food. No npm install required. - Peers who get it. Bring your worst outage story; someone will always one-up it. - Zero slides. Zero pitch. Zero on-call pages (we checked).

Hosted by Rubrik. Advance registration required .

```json
{"day": "2026-10-28", "start": "17:30", "end": "20:30",
 "title": "Recovery Hour with Rubrik", "room": "Barrio",
 "speaker": "",
 "note": "Join Rubrik at Barrio for drinks, bites, and the kind of hallway conversations that never fit in a session slot."}
```

#### Ship & Sip

**Wednesday, Oct 28 · 5:30 PM - 8:30 PM PDT**  
**Where:** The Interval @ Long Now Fort Mason Center Building A  
**Type:** Social

Sentry and LaunchDarkly are taking over The Interval on October 28th, 5:30–7:30pm. Water views, good bites, and 70 developers who'd rather talk about what they're building than what they're selling. No talks, no demos, no pitch - just bring what you shipped this year, or what you keep meaning to ship.

Hosted by Sentry and LaunchDarkly. Advance registration required .

```json
{"day": "2026-10-28", "start": "17:30", "end": "20:30",
 "title": "Ship & Sip", "room": "The Interval",
 "speaker": "",
 "note": "Sentry and LaunchDarkly are taking over The Interval on October 28th, 5:30-7:30pm."}
```

### 6:00 PM

#### Builders on the Green

**Wednesday, Oct 28 · 6:00 PM - 8:30 PM PDT**  
**Where:** Subpar Miniature Golf @ 900 North Point St  
**Type:** Social

Join Mintlify for an evening of mini golf, arcade games, drinks, and good conversation during GitHub Universe. We’re bringing together a curated group of engineering, developer, and technical leaders for a relaxed night away from the conference floor. No panels, no pitches, just a chance to meet other people building and leading technical teams. We’ll have the space to ourselves with unlimited golf + arcade games, plus plenty of time to hang out, grab a drink, and take in views of Alcatraz from the patio. Space is limited and attendance will be curated to create a great mix of builders and technical leaders.

Hosted by Mintlify. Advance registration required .

```json
{"day": "2026-10-28", "start": "18:00", "end": "20:30",
 "title": "Builders on the Green", "room": "Subpar Miniature Golf",
 "speaker": "",
 "note": "Join Mintlify for an evening of mini golf, arcade games, drinks, and good conversation during GitHub Universe."}
```

#### DevOps on Draft: A Universe Git-Together

**Wednesday, Oct 28 · 6:00 PM - 9:00 PM PDT**  
**Where:** San Francisco Brewing Co. @ 3150 Polk St  
**Type:** Social

Keep the fun going after the first full day of GitHub Universe! Join us at San Francisco Brewing Company for great food, local craft beer, a live DJ, and plenty of good company. Catch up with familiar faces, meet new people, and connect with fellow developers and technology leaders. Challenge someone to a game of pool or shuffleboard, hit the dance floor, and capture the night in the photo booth. Space is limited, so save your spot and come raise a glass with us! Hosted by Cloudsmith, Chainguard, Eficode, Octopus Deploy, and Tailscale.

Hosted by Cloudsmith, Chainguard, Eficode, Octopus Deploy, and Tailscale. Advance registration required .

```json
{"day": "2026-10-28", "start": "18:00", "end": "21:00",
 "title": "DevOps on Draft: A Universe Git-Together", "room": "San Francisco Brewing Co.",
 "speaker": "",
 "note": "Join us at San Francisco Brewing Company for great food, local craft beer, a live DJ, and plenty of good company."}
```

#### Happy Hour with Insight

**Wednesday, Oct 28 · 6:00 PM - 9:00 PM PDT**  
**Where:** Bar Darling @ 2263 Chestnut St  
**Type:** Social

Keep the conversation going after Day 1 of GitHub Universe. Join Insight at Bar Darling for cocktails, appetizers and an opportunity to connect with technology leaders, developers, engineering teams, and GitHub experts.

Hosted by Insight. Advance registration required .

```json
{"day": "2026-10-28", "start": "18:00", "end": "21:00",
 "title": "Happy Hour with Insight", "room": "Bar Darling",
 "speaker": "",
 "note": "Join Insight at Bar Darling for cocktails, appetizers and an opportunity to connect with technology leaders, developers, engineering..."}
```

#### Xebia's Broad Street Oyster Bash

**Wednesday, Oct 28 · 6:00 PM - 9:00 PM PDT**  
**Where:** Broad Street Oyster Co @ 900 North Point St  
**Type:** Social

After a full day at GitHub Universe, join us to shuck, sip, and unwind by the water. With the bright, coastal energy of San Francisco’s waterfront as the backdrop, Broad Street Oyster Co is the perfect spot for an evening of oysters, conversation, and connections that flow as easily as the drinks. Where: Broad Street Oyster Co, 900 North Point St Suite #K201, San Francisco Why Attend: - Bright, laid-back coastal atmosphere to unwind after a full day at GitHub Universe - Relaxed conversations about scaling AI, platform modernization, and developer productivity - Leverage insights from GitHub’s two time Partner of the Year winners on real-world experience in helping teams turn innovation into impact What to Expect: - Fresh oysters and local bites (yes, the famous lobster rolls) - Wine, beer, cocktails, and N/A options - Meet peers and leaders against the backdrop of bay views and San Francisco’s coastal energy.

Hosted by Xebia. Advance registration required .

```json
{"day": "2026-10-28", "start": "18:00", "end": "21:00",
 "title": "Xebia's Broad Street Oyster Bash", "room": "Broad Street Oyster Co",
 "speaker": "",
 "note": "After a full day at GitHub Universe, join us to shuck, sip, and unwind by the water."}
```

#### Bitrise Connect San Francisco

**Wednesday, Oct 28 · 6:00 PM - 10:00 PM PDT**  
**Where:** Flores San Francisco @ 2030 Union St  
**Type:** Social

Join us for a private evening built around one question: what does it actually take to scale mobile apps without compromising on speed? This is a small, curated gathering for mobile engineering leaders. No conference crowd, no sales pitches — just great conversations with the people shaping the future of mobile.

Hosted by Bitrise. Advance registration required .

```json
{"day": "2026-10-28", "start": "18:00", "end": "22:00",
 "title": "Bitrise Connect San Francisco", "room": "Flores San Francisco",
 "speaker": "",
 "note": "Join us for a private evening built around one question: what does it actually take to scale mobile apps without compromising on speed?"}
```

#### Exclusive Live Cooking Experience for Security Leaders

**Wednesday, Oct 28 · 6:00 PM - 10:00 PM PDT**  
**Where:** The Civic Kitchen @ 2961 Mission St  
**Type:** Social

Join a select group of Security & DevOps Leaders for a hands-on evening celebrating Slavic culinary traditions. Together with a professional chef, we’ll learn how to make traditional varenyky/pierogis from scratch — from rolling and stuffing to folding and pinching. Once the build phase is complete, we’ll sit down to enjoy the results, paired with great drinks and even better conversations. No sales pitches. No slide decks. Just good food, relaxed networking, and great people. What to expect: - Welcome & socializing — drinks and appetizers to kick off the evening - Hands-on cooking workshop — make traditional dumplings with a professional chef - Dinner & networking — enjoy what you’ve created and connect with fellow Security & DevOps leaders Why join? - Hands-on experience: Learn a traditional recipe you can recreate at home. - Peer-to-peer connections: Meet fellow Security Leaders, DevOps professionals, and CISOs in a relaxed setting. - A chance to unwind: Take a break from the conference schedule and enjoy an evening away from screens and slides. Limited spots The event is intentionally small to keep the workshop interactive and the atmosphere relaxed. RSVPs are subject to confirmation. About GitProtect GitProtect brings 16+ years of enterprise backup expertise to DevOps, helping organizations protect mission-critical data across their DevOps stack — from repositories and metadata to critical project management data.

Hosted by GitProtect.io. Advance registration required .

```json
{"day": "2026-10-28", "start": "18:00", "end": "22:00",
 "title": "Exclusive Live Cooking Experience for Security Leaders", "room": "The Civic Kitchen",
 "speaker": "",
 "note": "Join a select group of Security & DevOps Leaders for a hands-on evening celebrating Slavic culinary traditions."}
```

## Thursday, Oct 29

### 8:00 AM

#### Volunteer with GitHub Gives

**Thursday, Oct 29 · 8:00 AM - 9:00 AM PDT**  
**Where:** Equator Coffee @ Fort Mason  
**Type:** Social

Start day two of Universe by giving back to our host city. Join GitHub Gives and local nonprofit Refuse Refuse for a community cleanup around Fort Mason Center. Meet directly across the road from Equator Coffee at 8:00 a.m. PT for an introduction from Refuse Refuse before the group heads out for the cleanup. Please wear closed-toe shoes, dress for the weather, and bring a jacket - the San Francisco waterfront can be chilly. Connect with fellow attendees while taking action together to help keep San Francisco clean and beautiful.

```json
{"day": "2026-10-29", "start": "08:00", "end": "09:00",
 "title": "Volunteer with GitHub Gives", "room": "Equator Coffee",
 "speaker": "",
 "note": "Join GitHub Gives and local nonprofit Refuse Refuse for a community cleanup around Fort Mason Center."}
```

### 9:00 AM

#### Building domain-specific AI agents for hardware reliability at NVIDIA

**Thursday, Oct 29 · 9:00 AM - 9:15 AM PDT**  
**Where:** Ship & Tell @ Firehouse  
**Type:** Ship & Tell · **Format:** In-person, Recorded, AI summary

GitHub Copilot catches surface-level issues. But what about hardware-specific constraints, firmware interactions, and system-level failures? For teams working on hardware-software systems, AI adoption is significantly more complex than in pure software environments.

Maria Victoria Gromysch shares a practical framework developed at NVIDIA for integrating AI across the full engineering lifecycle: test generation at pre-commit, AI-assisted code review at commit time, and system validation in CI/CD.

You'll also learn how to build domain-specific agents trained on internal logs and diagnostics, design a layered AI workflow, identify where general-purpose tools fall short, and close the feedback loop between production failures and model improvement.

**Speakers**

- Maria Victoria Gromysch: Test Engineer, NVIDIA

```json
{"day": "2026-10-29", "start": "09:00", "end": "09:15",
 "title": "Building domain-specific AI agents for hardware reliability at NVIDIA", "room": "Ship & Tell",
 "speaker": "Maria Victoria Gromysch (NVIDIA)",
 "note": "GitHub Copilot catches surface-level issues. But what about hardware-specific constraints, firmware interactions, and system-level failures?"}
```

#### Opening the black box: Tracing, debugging, and fixing your GitHub Actions agents (Sponsored)

**Thursday, Oct 29 · 9:00 AM - 9:15 AM PDT**  
**Where:** Demos & Donuts @ Gateway Pavilion, Level 2  
**Type:** Product Demo · **Format:** In-person, AI summary

GitHub Actions has become home to a whole generation of custom agents: triaging issues, iterating on pull requests, reviewing diffs. But when one misbehaves, you get a green check or a red X and nothing else. Agent tracing from Sentry show you what actually happened: which tool calls errored, how long each step of the workflow took, how many tokens got consumed, and where to optimize next. Connect Copilot to Sentry's MCP server to pull that data on demand, or build your own automations with Sentry as the source of production agent traces for evals and debugging. You'll leave this session knowing how to turn a silent pass/fail into a full trace you can debug, and how to feed real production data back into improving your agents.

**Speakers**

- Serge Dybskiy: Developer Experience Engineer, Sentry

```json
{"day": "2026-10-29", "start": "09:00", "end": "09:15",
 "title": "Opening the black box: Tracing, debugging, and fixing your GitHub Actions agents (Sponsored)", "room": "Demos & Donuts (Level 2)",
 "speaker": "Serge Dybskiy (Sentry)",
 "note": "You'll leave this session knowing how to turn a silent pass/fail into a full trace you can debug, and how to feed real production data..."}
```

#### The view from the labs: What's next for AI-assisted development

**Thursday, Oct 29 · 9:00 AM - 9:30 AM PDT**  
**Where:** Main Stage @ Festival Pavilion  
**Type:** Main Stage · **Format:** In-person, Recorded, AI summary

The people building frontier AI models see early signals about where capabilities are heading and which skills and workflows are about to matter more or require a shift. This interactive panel brings together leaders from the major frontier model labs (Anthropic, OpenAI, and Google Cloud) that power GitHub Copilot for the conversation developers actually want: a candid, forward-looking discussion about what the next two years of AI-assisted development look like, and what that means for the people in the room.

**Speakers**

- Rohan Varma: Product Lead, Enterprise Agents, OpenAI
- April Leonard: VP, Engineering, GitHub
- Richard Seroter: Senior Director and Chief Evangelist, Google Cloud
- Angela Jiang: Head of Product, Claude Platform, Anthropic

```json
{"day": "2026-10-29", "start": "09:00", "end": "09:30",
 "title": "The view from the labs: What's next for AI-assisted development", "room": "Main Stage",
 "speaker": "Rohan Varma (OpenAI), April Leonard (GitHub), Richard Seroter (Google Cloud), Angela Jiang (Anthropic)",
 "note": "The people building frontier AI models see early signals about where capabilities are heading and which skills and workflows are about..."}
```

#### Beyond pass or fail: How agents verify AI-generated code (Sponsored)

**Thursday, Oct 29 · 9:00 AM - 9:40 AM PDT**  
**Where:** Silent Disco Breakouts @ Festival Pavilion  
**Type:** Breakout Session · **Format:** In-person, AI summary

Your coding agent just shipped a feature. The tests pass, but does the feature work as intended? 

This session shows how agents can go beyond scripted checks to explore an application in a real browser, investigate unexpected behavior, and keep tests current as the product changes. You’ll see how they gather evidence, reproduce failures, and distinguish product bugs from broken tests or infrastructure problems. 

You’ll also learn how deterministic controls keep agents within safe boundaries, and leave with a practical framework for deciding what agents should test, what code should control, and when a human needs to step in.

**Speakers**

- Jeff An: CTO & Co-founder, Momentic

```json
{"day": "2026-10-29", "start": "09:00", "end": "09:40",
 "title": "Beyond pass or fail: How agents verify AI-generated code (Sponsored)", "room": "Silent Disco Breakouts",
 "speaker": "Jeff An (Momentic)",
 "note": "This session shows how agents can go beyond scripted checks to explore an application in a real browser, investigate unexpected..."}
```

#### Scaling GitHub’s infrastructure for how developers build today

**Thursday, Oct 29 · 9:00 AM - 9:40 AM PDT**  
**Where:** Cowell Theater @ Gateway Pavilion  
**Type:** Breakout Session · **Format:** In-person, AI summary

We share how GitHub is evolving its infrastructure to take on more concurrent work from developers, automations, and agents. That evolution includes a new storage architecture for Git repository data. Explore the engineering behind this work, the journey it's taken to get there, what it means for your teams, and how it strengthens GitHub's foundation for the next generation of software development.

**Speakers**

- Brian Celenza: Principal Software Engineer, GitHub

```json
{"day": "2026-10-29", "start": "09:00", "end": "09:40",
 "title": "Scaling GitHub's infrastructure for how developers build today", "room": "Cowell Theater",
 "speaker": "Brian Celenza (GitHub)",
 "note": "Explore the engineering behind this work, the journey it's taken to get there, what it means for your teams, and how it strengthens..."}
```

#### Visa's Zero-Secrets Initiative: no hardcoded secrets, no exceptions

**Thursday, Oct 29 · 9:00 AM - 9:40 AM PDT**  
**Where:** BATS Theatre @ Fort Mason Building B, 3rd Floor  
**Type:** Breakout Session · **Format:** In-person, AI summary

Visa’s policy is simple: no credentials in source code, ever. Turning that into something that actually runs across a global engineering organization took a full procedure, not a feature toggle.

This session walks the path end to end. First, detection: automated scanning for credentials across our whole estate. Next, the procedure we built around it: how alerts get routed and prioritized, who owns a finding, and why the fix is revoking and rotating the credential rather than only deleting the line of code. Then, prevention: stopping a push that carries a secret, and the governed exception path that sits alongside it. And throughout, how automation cuts the alert load, with AI assisting on the human side of a finding rather than on the secret itself.

Enforcing a zero secrets policy at scale is a massive operational challenge. You will leave this session with the sequence we used, what we learned along the way, and the parts that can be reused in your own organization.

**Speakers**

- Kautilay Siingh: Security Architect, VISA
- Sanjeev Murthy: Director, Cybersecurity, Visa

```json
{"day": "2026-10-29", "start": "09:00", "end": "09:40",
 "title": "Visa's Zero-Secrets Initiative: no hardcoded secrets, no exceptions", "room": "BATS Theatre, 3rd Floor",
 "speaker": "Kautilay Siingh (VISA), Sanjeev Murthy (Visa)",
 "note": "This session walks the path end to end."}
```

#### Stop prompting, start delegating: Configure Copilot to own the work

**Thursday, Oct 29 · 9:00 AM - 9:45 AM PDT**  
**Where:** Sandbox @ Fort Mason Building C, Founders Inc., 3rd Floor  
**Type:** Sandbox Session · **Format:** In-person

Your repository's Copilot configuration may be all that stands between you and trusting AI to handle complex tasks on its own. In this session, Ken Muse and Mickey Gousset demonstrate how to enhance a TypeScript app by layering GitHub Copilot's full stack, showing how each capability reinforces the last. 

You'll see exactly how Copilot spends context and tokens, with before-and-after comparisons that make the efficiency gains measurable. You'll leave with a working project and an understanding of which Copilot capability fits which task, so you can delegate more and prompt less.

**Speakers**

- Mickey Gousset: Staff DevOps Architect | ODST | FDE, GitHub
- Ken Muse: Staff DevOps Architect | ODST | FDE, GitHub

```json
{"day": "2026-10-29", "start": "09:00", "end": "09:45",
 "title": "Stop prompting, start delegating: Configure Copilot to own the work", "room": "Sandbox, 3rd Floor",
 "speaker": "Mickey Gousset (GitHub), Ken Muse (GitHub)",
 "note": "Ken Muse and Mickey Gousset demonstrate how to enhance a TypeScript app by layering GitHub Copilot's full stack, showing how each..."}
```

#### Admin readiness for AI usage management

**Thursday, Oct 29 · 9:00 AM - 10:30 AM PDT**  
**Where:** Workshops @ Gateway Pavilion, Level 1  
**Type:** Workshop · **Format:** In-person

Enterprise administrators are increasingly expected to explain Copilot adoption, spending, and governance to leadership, finance, and security. In this interactive workshop, participants step into the role of a Copilot administrator responding to three realistic stakeholder inquiries.

Using enterprise and organization scenarios, attendees will explore how to assess usage and adoption, understand how spending maps to the organization, and review the policies and access decisions that shape Copilot management. They will practice navigating administrative settings, interpreting organizational data, understanding the scope of controls, and preparing clear responses for each stakeholder group.

The session concludes with a practical action plan focused on adoption, spending, and governance. Participants leave with a repeatable playbook for answering executive questions and making informed Copilot administration decisions across the enterprise.

**Speakers**

- Abel Berhane: Sr Service Delivery Engineer, GitHub
- Vanessa Minik: Senior Service Delivery Engineer, GitHub

```json
{"day": "2026-10-29", "start": "09:00", "end": "10:30",
 "title": "Admin readiness for AI usage management", "room": "Workshops (Level 1)",
 "speaker": "Abel Berhane (GitHub), Vanessa Minik (GitHub)",
 "note": "The session concludes with a practical action plan focused on adoption, spending, and governance."}
```

### 9:05 AM

#### Agentic Workflows: Automation at scale

**Thursday, Oct 29 · 9:05 AM - 9:35 AM PDT**  
**Where:** The Speakeasy @ GitHub Central, Festival Pavilion  
**Type:** Breakout Session · **Format:** In-person, AI summary

Automation is how we buy time for craft, enforce correctness in situations that require judgment, and improve our software at business scale. Learn how to start automating, as well as how you can start to setup your software factory with governance, monitoring, and security so you can roll out automations to everyone in your business!

**Speakers**

- Landon Cox: Senior Principle Researcher, Microsoft
- Peli de Halleux: Agentic Engineer, GitHub Next, Microsoft

```json
{"day": "2026-10-29", "start": "09:05", "end": "09:35",
 "title": "Agentic Workflows: Automation at scale", "room": "The Speakeasy (GitHub Central)",
 "speaker": "Landon Cox (Microsoft), Peli de Halleux (Microsoft)",
 "note": "Learn how to start automating, as well as how you can start to setup your software factory with governance, monitoring, and security so..."}
```

### 9:15 AM

#### GitHub configuration as code: Scaling org management with Terraform

**Thursday, Oct 29 · 9:15 AM - 9:30 AM PDT**  
**Where:** Silent Disco Demos @ Festival Pavilion  
**Type:** Product Demo · **Format:** In-person, Recorded, AI summary

As organizations scale, GitHub configurations can become increasingly complex to manage. Restrict admin access too tightly and development slows. Loosen it too much and security risks increase.

This session shows how one team solved this by codifying critical GitHub configurations through Terraform, with every change proposed and reviewed through pull requests. Over three years, more than 800 configuration changes have been managed through this model, preserving both governance and developer autonomy.

You'll learn how to manage configurations, automate routine requests with Copilot, ensure traceability and governance for every change through pull request-based workflows, and leverage accumulated IaC knowledge for practical AI agent adoption.

**Speakers**

- Yasuhiro Osaki: Software Engineer, Sony

```json
{"day": "2026-10-29", "start": "09:15", "end": "09:30",
 "title": "GitHub configuration as code: Scaling org management with Terraform", "room": "Silent Disco Demos",
 "speaker": "Yasuhiro Osaki (Sony)",
 "note": "This session shows how one team solved this by codifying critical GitHub configurations through Terraform, with every change proposed..."}
```

### 9:20 AM

#### AI agents write the code. Novus decides what to build next. (Sponsored)

**Thursday, Oct 29 · 9:20 AM - 9:35 AM PDT**  
**Where:** Demos & Donuts @ Gateway Pavilion, Level 2  
**Type:** Product Demo · **Format:** In-person, AI summary

Coding agents can write and ship software quickly, but teams still need to know what to build and which user problems matter most. In this demo, Pendo’s Head of Product shows how Novus, the product agent that connects user behavior to the codebase, identifies product opportunities, finds UX issues, and recommends what teams and coding agents should work on next. You’ll see Novus turn product signals into action: surfacing an issue, proposing a fix, and connecting that work to the codebase. This demo also shows how to use AI to move from product discovery to development, while keeping teams focused on the updates that users care about.

**Speakers**

- Tiffany Kitchen: Head of Product, Pendo

```json
{"day": "2026-10-29", "start": "09:20", "end": "09:35",
 "title": "AI agents write the code. Novus decides what to build next. (Sponsored)", "room": "Demos & Donuts (Level 2)",
 "speaker": "Tiffany Kitchen (Pendo)",
 "note": "Pendo's Head of Product shows how Novus, the product agent that connects user behavior to the codebase, identifies product..."}
```

### 9:30 AM

#### The 2am RCA Agent: Architecting AI that investigates, not hallucinates

**Thursday, Oct 29 · 9:30 AM - 9:45 AM PDT**  
**Where:** Ship & Tell @ Firehouse  
**Type:** Ship & Tell · **Format:** In-person, Recorded, AI summary

At 2 am, an alert fires. You spend 90 minutes jumping between Grafana, Jaeger, and logs, correlating by hand, fighting confirmation bias, and writing the RCA doc backwards. Achin Gupta and Divya Mahajan built an agent that does this in seconds. 

Surprisingly, the LLM only handles 4 of 10 nodes. Signal fetching, BFS topology traversal, correlation, and scoring are fully deterministic, which means they’re auditable, replayable, and cheap. The LLM narrates the evidence rather than gathering it. 

In this session, you'll see the architecture, a live demo of an alert-to-RCA report in seconds, and the design principles that make the system trustworthy in production. All code is open source; the paper is published on Zenodo. You'll leave with a blueprint for building agents you can actually trust in the middle of the night.

**Speakers**

- Achin Gupta: Staff Software Engineer, Intuit
- Divya Mahajan: Software Development Engineer, Amazon

```json
{"day": "2026-10-29", "start": "09:30", "end": "09:45",
 "title": "The 2am RCA Agent: Architecting AI that investigates, not hallucinates", "room": "Ship & Tell",
 "speaker": "Achin Gupta (Intuit), Divya Mahajan (Amazon)",
 "note": "You'll see the architecture, a live demo of an alert-to-RCA report in seconds, and the design principles that make the system..."}
```

### 9:35 AM

#### When a prototype becomes critical, does your GitHub policy know? (Sponsored)

**Thursday, Oct 29 · 9:35 AM - 9:50 AM PDT**  
**Where:** Silent Disco Demos @ Festival Pavilion  
**Type:** Product Demo · **Format:** In-person, Recorded, AI summary

What happens when a prototype goes into production and starts handling real customer payments, but its GitHub repository still carries the merge requirements it launched with? 

In this session, Baruch Sadogursky shares how he syncs ownership and business criticality from Port into GitHub as custom properties, making it possible to find repositories by owning team and point a GitHub ruleset at critical services. 

You'll watch that gap close live, and leave with a repeatable pattern: Port supplies the context, and GitHub turns that context into enforced policy.

**Speakers**

- Baruch Sadogursky: Head of Developer Relations, Port.io

```json
{"day": "2026-10-29", "start": "09:35", "end": "09:50",
 "title": "When a prototype becomes critical, does your GitHub policy know? (Sponsored)", "room": "Silent Disco Demos",
 "speaker": "Baruch Sadogursky (Port.io)",
 "note": "Baruch Sadogursky shares how he syncs ownership and business criticality from Port into GitHub as custom properties, making it possible..."}
```

### 9:40 AM

#### Resolve your security alerts faster with GitHub Copilot

**Thursday, Oct 29 · 9:40 AM - 9:55 AM PDT**  
**Where:** Demos & Donuts @ Gateway Pavilion, Level 2  
**Type:** Product Demo · **Format:** In-person, AI summary

Security debt keeps growing: more code, more tools, more pressure to ship fast. Most teams are staring at an alert backlog nobody has time to work through.

Agentic autofix helps you reduce the amount of time it takes to resolve your security alerts. It generates mergeable fixes for them in minutes, so remediation becomes a pull request review instead of a multi-day investigation.

In this session, you'll see it in action through a live demo, plus what we've learned from our customers using it. You'll leave knowing how to put it to work in your own workflow.

**Speakers**

- Jon Janego: Senior Product Manager, GitHub
- Carlin Cherry: Senior Product Manager, GitHub

```json
{"day": "2026-10-29", "start": "09:40", "end": "09:55",
 "title": "Resolve your security alerts faster with GitHub Copilot", "room": "Demos & Donuts (Level 2)",
 "speaker": "Jon Janego (GitHub), Carlin Cherry (GitHub)",
 "note": "You'll see it in action through a live demo, plus what we've learned from our customers using it."}
```

### 9:45 AM

#### Session After Party: The view from the labs: What's next for AI-assisted development

**Thursday, Oct 29 · 9:45 AM - 10:15 AM PDT**  
**Where:** The Speakeasy @ GitHub Central, Festival Pavilion  
**Type:** Session After Party · **Format:** In-person

This is an informal follow-up Q&A to the main stage session "The view from the labs: What's next for AI-assisted development." Right after the panel, join the speakers for the session in GitHub Central. Bring your questions and keep the conversation going.

**Speakers**

- April Leonard: VP, Engineering, GitHub
- Rohan Varma: Product Lead, Enterprise Agents, OpenAI
- Richard Seroter: Senior Director and Chief Evangelist, Google Cloud

```json
{"day": "2026-10-29", "start": "09:45", "end": "10:15",
 "title": "Session After Party: The view from the labs: What's next for AI-assisted development", "room": "The Speakeasy (GitHub Central)",
 "speaker": "April Leonard (GitHub), Rohan Varma (OpenAI), Richard Seroter (Google Cloud)",
 "note": "This is an informal follow-up Q&A to the main stage session \"The view from the labs: What's next for AI-assisted development.\" Right..."}
```

### 9:50 AM

#### What's worth building when AI can build anything?

**Thursday, Oct 29 · 9:50 AM - 10:20 AM PDT**  
**Where:** Main Stage @ Festival Pavilion  
**Type:** Main Stage · **Format:** In-person, Recorded, AI summary

AI can build almost anything you ask it to, which makes a harder question unavoidable: what's actually worth building? In this conversation, Sue Black of Durham University and Kent C. Dodds of kody.codes make the case for building deliberately rather than reflexively. 

This session will explore what responsible software looks like and take a deeper dive into the daily reality of shipping, choosing between tools, and maintaining what’s already built. You'll leave with a sharper set of questions to bring to your own work, along with a clearer sense of when speed is worth it and when it isn't.

**Speakers**

- Kent C. Dodds: Product Engineer, kody.codes
- Sue Black: Professor of Computer Science and Technology Evangelist, Durham University

```json
{"day": "2026-10-29", "start": "09:50", "end": "10:20",
 "title": "What's worth building when AI can build anything?", "room": "Main Stage",
 "speaker": "Kent C. Dodds (kody.codes), Sue Black (Durham University)",
 "note": "This session will explore what responsible software looks like and take a deeper dive into the daily reality of shipping, choosing..."}
```

### 9:55 AM

#### IBM Neo: From specifications to verified software delivery (Sponsored)

**Thursday, Oct 29 · 9:55 AM - 10:10 AM PDT**  
**Where:** Silent Disco Demos @ Festival Pavilion  
**Type:** Product Demo · **Format:** In-person, Recorded, AI summary

See how IBM Neo brings together specification-driven development, AI agents, and proof-based validation across the software delivery lifecycle. In this live demo, learn how teams set direction, evaluate evidence, and intervene at key decision points while agents work toward verifiable outcomes.

**Speakers**

- Josh Scriven: Microsoft Americas Practice, AI Leader, IBM Consulting
- Jihan Thomas: Chief AI Architect, IBM

```json
{"day": "2026-10-29", "start": "09:55", "end": "10:10",
 "title": "IBM Neo: From specifications to verified software delivery (Sponsored)", "room": "Silent Disco Demos",
 "speaker": "Josh Scriven (IBM Consulting), Jihan Thomas (IBM)",
 "note": "See how IBM Neo brings together specification-driven development, AI agents, and proof-based validation across the software delivery..."}
```

### 10:00 AM

#### Delete the wiki: An MCP platform that closes its own loop

**Thursday, Oct 29 · 10:00 AM - 10:15 AM PDT**  
**Where:** Ship & Tell @ Firehouse  
**Type:** Ship & Tell · **Format:** In-person, Recorded, AI summary

Wikis promise discoverability. Portals promise self-service. Both start rotting the moment a story closes and the docs stop matching reality.

So the team stopped writing docs by hand and built a platform that writes them itself: an MCP-powered loop where AI agents read live infrastructure context to ship real work, then write that context back the moment a story is done, as docs, diagrams, tech-debt records, and follow-up tasks. The documentation stays current because producing it is part of doing the work, not a chore that happens after.

This session will demo the full loop end to end: provisioning a codespace from intent, then watching the agent ship the change, file the docs, log the tech debt, and refresh the architecture diagram on its own. You'll leave with the patterns that make a platform self-healing instead of self-rotting, and a clear sense of how to close the loop between doing the work and documenting it on your own stack.

**Speakers**

- Sumanth Mothkuri: Sr. Platform Engineer, Equifax
- Hrushikesh Pokala: Sr Software Engineer - Lead, Equifax

```json
{"day": "2026-10-29", "start": "10:00", "end": "10:15",
 "title": "Delete the wiki: An MCP platform that closes its own loop", "room": "Ship & Tell",
 "speaker": "Sumanth Mothkuri (Equifax), Hrushikesh Pokala (Equifax)",
 "note": "This session will demo the full loop end to end: provisioning a codespace from intent, then watching the agent ship the change, file the..."}
```

#### How to ship fast, measure impact, and know when to intervene in the AI era (Sponsored)

**Thursday, Oct 29 · 10:00 AM - 10:15 AM PDT**  
**Where:** Demos & Donuts @ Gateway Pavilion, Level 2  
**Type:** Product Demo · **Format:** In-person, AI summary

Coding agents can help teams ship features in hours, but a fast release doesn’t tell you whether a change worked. This session introduces Statsig, a platform for managing feature gates, experiments, and product metrics, and shows how teams can use it to measure the impact of their releases. A live demo will illustrate how staged rollouts, guardrail metrics, experiments, and automated responses to regressions help teams learn from releases sooner—and what to do when a metric changes unexpectedly. You’ll leave with a practical approach for measuring release impact, catching regressions earlier, and making better decisions about what to ship next.

**Speakers**

- Jacob Newman: Principal Product Manager, Amplitude
- Madelyn Tarr: Sr Product Manager, Amplitude / Statsig

```json
{"day": "2026-10-29", "start": "10:00", "end": "10:15",
 "title": "How to ship fast, measure impact, and know when to intervene in the AI era (Sponsored)", "room": "Demos & Donuts (Level 2)",
 "speaker": "Jacob Newman (Amplitude), Madelyn Tarr (Amplitude / Statsig)",
 "note": "This session introduces Statsig, a platform for managing feature gates, experiments, and product metrics, and shows how teams can use it..."}
```

#### From AI-assisted work to agent-enabled delivery: Scaling AI across product teams

**Thursday, Oct 29 · 10:00 AM - 10:40 AM PDT**  
**Where:** Cowell Theater @ Gateway Pavilion  
**Type:** Breakout Session · **Format:** In-person, AI summary

What if scaling AI across product teams worked like a game: moving through levels, unlocking criteria, and progressing clearly? Vanguard is improving how more than 800 cross-functional product teams operate by applying a structured AI maturity framework across the product development lifecycle.

This session shares where the team is now, the capabilities being scaled today, and lessons on how organizations can progress from AI-assisted work toward agent-enabled delivery.

**Speakers**

- Brendan Bergen: Director, AI Enablement, Vanguard
- Ryan Platt: Senior Cloud Architect, Vanguard

```json
{"day": "2026-10-29", "start": "10:00", "end": "10:40",
 "title": "From AI-assisted work to agent-enabled delivery: Scaling AI across product teams", "room": "Cowell Theater",
 "speaker": "Brendan Bergen (Vanguard), Ryan Platt (Vanguard)",
 "note": "This session shares where the team is now, the capabilities being scaled today, and lessons on how organizations can progress from..."}
```

#### Write-only code: What happens to peer review when agents write the diffs

**Thursday, Oct 29 · 10:00 AM - 10:40 AM PDT**  
**Where:** BATS Theatre @ Fort Mason Building B, 3rd Floor  
**Type:** Breakout Session · **Format:** In-person, AI summary

Peer review was how engineers learned: juniors got sharper, seniors stayed honest. Then agents wrote the code, and reviewing each other turned into auditing machines. That's why it felt awful. 

On separate teams, Adam Jacob and Dylan Ratcliffe each found the same fix: stop reviewing the code and review the plan a human writes before the agent builds. The human loop came back, and now they enjoy the work again. 

This talk is the two of them comparing notes and disagreeing hard on one thing: whether review stops mattering once software is no longer a garden you tend for people. You'll leave knowing how to move review upstream on your own team, with a clear view of what you keep and what you give up.

**Speakers**

- Dylan Ratcliffe: Founder & CEO, Overmind
- Adam Jacob: CEO and Co-Founder, Swamp Club

```json
{"day": "2026-10-29", "start": "10:00", "end": "10:40",
 "title": "Write-only code: What happens to peer review when agents write the diffs", "room": "BATS Theatre, 3rd Floor",
 "speaker": "Dylan Ratcliffe (Overmind), Adam Jacob (Swamp Club)",
 "note": "This talk is the two of them comparing notes and disagreeing hard on one thing: whether review stops mattering once software is no..."}
```

#### Your agents write the fix. Observability supplies the context. (Sponsored)

**Thursday, Oct 29 · 10:00 AM - 10:40 AM PDT**  
**Where:** Silent Disco Breakouts @ Festival Pavilion  
**Type:** Breakout Session · **Format:** In-person, AI summary

Your agent’s pull request passed CI and merged. But will the fix hold up under real traffic? In this live demo, you’ll see Bluebox by Dynatrace use OpenTelemetry data to brief a coding agent on a microservice app. When the app breaks, the agent opens a pull request with an evidence-backed diagnosis and proposed fix. After review and deployment, the team checks error rates and SLOs for regressions. You’ll leave with a practical model for verifying agent-written changes and deciding where human review, escalation, and a kill switch belong.

**Speakers**

- Andrew Norris: Director, Product Management of Bluebox.ai, Bluebox.ai by Dynatrace
- Michael Beemer: Principle Product Manager, Dynatrace

```json
{"day": "2026-10-29", "start": "10:00", "end": "10:40",
 "title": "Your agents write the fix. Observability supplies the context. (Sponsored)", "room": "Silent Disco Breakouts",
 "speaker": "Andrew Norris (Bluebox.ai by Dynatrace), Michael Beemer (Dynatrace)",
 "note": "You'll leave with a practical model for verifying agent-written changes and deciding where human review, escalation, and a kill switch..."}
```

### 10:15 AM

#### Build and run AI locally with NVIDIA (Sponsored)

**Thursday, Oct 29 · 10:15 AM - 10:30 AM PDT**  
**Where:** Silent Disco Demos @ Festival Pavilion  
**Type:** Product Demo · **Format:** In-person, Recorded, AI summary

What does it take to get an AI application running on your own hardware? This session explores how GitHub Copilot and NVIDIA developer tools support local development across RTX laptops and desktops, RTX PRO workstations, DGX Spark and DGX Station AI supercomputers. Learn where GPU-accelerated frameworks, optimized recipes, and SDKs fit when running coding agents, customizing models, and building applications. A live demo shows Copilot helping launch a local model with llama.cpp. You’ll leave with a practical starting point for building AI apps with greater control over where inference runs.

**Speakers**

- Annamalai Chockalingam: Sr. Product Manager, Local AI Developers, NVIDIA

```json
{"day": "2026-10-29", "start": "10:15", "end": "10:30",
 "title": "Build and run AI locally with NVIDIA (Sponsored)", "room": "Silent Disco Demos",
 "speaker": "Annamalai Chockalingam (NVIDIA)",
 "note": "This session explores how GitHub Copilot and NVIDIA developer tools support local development across RTX laptops and desktops, RTX PRO..."}
```

#### How to turn your team's repeated workflows into GitHub Copilot CLI skills

**Thursday, Oct 29 · 10:15 AM - 11:00 AM PDT**  
**Where:** Sandbox @ Fort Mason Building C, Founders Inc., 3rd Floor  
**Type:** Sandbox Session · **Format:** In-person

Every team has workflows they repeat daily: pull request feedback, docs, onboarding, or release prep. Instead of copy-pasting prompts or relying on institutional knowledge, you can package that work into reusable GitHub Copilot CLI assets. 

In this hands-on Sandbox, Beatris Mendez Gandica and Jeremiah Isaacson take you through the full Copilot CLI customization stack, then guide you through building a skill from scratch. You'll leave with a working .github directory and a reference repository with examples you can apply to your own workflows.

**Speakers**

- Bea Mendez Gandica: CEO/Founder, Nuevo Foundation
- Jeremiah Isaacson: CTO, Nuevo Foundation

```json
{"day": "2026-10-29", "start": "10:15", "end": "11:00",
 "title": "How to turn your team's repeated workflows into GitHub Copilot CLI skills", "room": "Sandbox, 3rd Floor",
 "speaker": "Bea Mendez Gandica (Nuevo Foundation), Jeremiah Isaacson (Nuevo Foundation)",
 "note": "You'll leave with a working .github directory and a reference repository with examples you can apply to your own workflows."}
```

### 10:20 AM

#### How Microsoft AI builds coding models optimized for GitHub Copilot

**Thursday, Oct 29 · 10:20 AM - 10:35 AM PDT**  
**Where:** Demos & Donuts @ Gateway Pavilion, Level 2  
**Type:** Product Demo · **Format:** In-person, AI summary

Go behind the scenes with Microsoft AI to learn how it builds and optimizes coding models for GitHub Copilot. This session will explore what makes code-focused models different—from training and evaluation to performance, safety, and real-world developer feedback. You’ll hear how Microsoft AI is advancing model quality for the workflows developers care about most, and how those innovations show up in GitHub Copilot experiences used by millions of developers.

**Speakers**

- Julia Kasper: Product Manager, Microsoft
- Yanan Cai: Principal Product Manager, Microsoft

```json
{"day": "2026-10-29", "start": "10:20", "end": "10:35",
 "title": "How Microsoft AI builds coding models optimized for GitHub Copilot", "room": "Demos & Donuts (Level 2)",
 "speaker": "Julia Kasper (Microsoft), Yanan Cai (Microsoft)",
 "note": "This session will explore what makes code-focused models different - from training and evaluation to performance, safety, and real-world..."}
```

### 10:30 AM

#### Open PRs, don't merge them: Fine-grained authorization for hosted MCP servers

**Thursday, Oct 29 · 10:30 AM - 10:45 AM PDT**  
**Where:** Ship & Tell @ Firehouse  
**Type:** Ship & Tell · **Format:** In-person, Recorded, AI summary

Hosted MCP servers all work the same way: OAuth in, broad scope out. One global toggle decides which tools to expose, and every authenticated identity gets the full set. So every agent inherits everything its human can do.

Teams often want something more precise. Maybe an agent should open a pull request and leave the merge to a human. Today the upstream server can't express that, and you can't change it, because it isn't yours.

This session shows a pattern that works today: an identity-aware proxy that adds per-identity authorization in front of any hosted MCP server, no changes upstream. You'll see it live — Copilot opening a PR and leaving the merge to a reviewer, enforced per user — and you'll leave with a working pattern for the MCP servers your team already depends on.

**Speakers**

- Nick Taylor: Developer Advocate/Software Engineer, Pomerium

```json
{"day": "2026-10-29", "start": "10:30", "end": "10:45",
 "title": "Open PRs, don't merge them: Fine-grained authorization for hosted MCP servers", "room": "Ship & Tell",
 "speaker": "Nick Taylor (Pomerium)",
 "note": "This session shows a pattern that works today: an identity-aware proxy that adds per-identity authorization in front of any hosted MCP..."}
```

### 10:35 AM

#### Session After Party: What's worth building when AI can build anything?

**Thursday, Oct 29 · 10:35 AM - 11:05 AM PDT**  
**Where:** The Speakeasy @ GitHub Central, Festival Pavilion  
**Type:** Session After Party · **Format:** In-person

This is an informal follow-up Q&A to the main stage session "What's worth building when AI can build anything?" Right after the talk, join Sue Black (Durham University) and Kent C. Dodds (kody.codes) in GitHub Central. Bring your questions and keep the conversation going.

**Speakers**

- Kent C. Dodds: Product Engineer, kody.codes
- Sue Black: Professor of Computer Science and Technology Evangelist, Durham University

```json
{"day": "2026-10-29", "start": "10:35", "end": "11:05",
 "title": "Session After Party: What's worth building when AI can build anything?", "room": "The Speakeasy (GitHub Central)",
 "speaker": "Kent C. Dodds (kody.codes), Sue Black (Durham University)",
 "note": "This is an informal follow-up Q&A to the main stage session \"What's worth building when AI can build anything?\" Right after the talk..."}
```

### 10:40 AM

#### Automating PR quality with Copilot CLI and GitHub Actions

**Thursday, Oct 29 · 10:40 AM - 10:55 AM PDT**  
**Where:** Demos & Donuts @ Gateway Pavilion, Level 2  
**Type:** Product Demo · **Format:** In-person, AI summary

Pull requests are often where quality deteriorates, from missing documentation and weak tests to delayed security feedback. This product demo shows how GitHub Copilot CLI and GitHub Actions can generate documentation, create unit tests, and run security checks on every commit and pull request, helping teams improve quality without slowing developers down.

**Speakers**

- Simona Toader: Sr Software Global Black Belt, Microsoft

```json
{"day": "2026-10-29", "start": "10:40", "end": "10:55",
 "title": "Automating PR quality with Copilot CLI and GitHub Actions", "room": "Demos & Donuts (Level 2)",
 "speaker": "Simona Toader (Microsoft)",
 "note": "Pull requests are often where quality deteriorates, from missing documentation and weak tests to delayed security feedback."}
```

#### How GitHub secures open source

**Thursday, Oct 29 · 10:40 AM - 11:10 AM PDT**  
**Where:** Main Stage @ Festival Pavilion  
**Type:** Main Stage · **Format:** In-person, Recorded, AI summary

For the past six years, the GitHub Security Lab has worked to secure the open source ecosystem, and that work has surfaced a set of practical principles that hold up in the real world. The speakers will share what succeeded, what didn't, and the ideas that matter most. Keep it simple, so security is easy for developers to understand and implement. Make it delicious, so security improvements are something people actually want to adopt. And keep it social, because nothing beats the collective intelligence of the community, especially now that agents and skills can tap into and magnify that shared knowledge. The session closes by looking at how the recent wave of AI is reshaping open source security, and what the future looks like in that new world. You'll leave with principles you can apply to make security stick in your own projects and communities.

**Speakers**

- Bas Alberts: Principal Security Reseracher, GitHub
- Xavier René-Corail: Sr. Dir, Security Research, GitHub

```json
{"day": "2026-10-29", "start": "10:40", "end": "11:10",
 "title": "How GitHub secures open source", "room": "Main Stage",
 "speaker": "Bas Alberts (GitHub), Xavier Ren\u00e9-Corail (GitHub)",
 "note": "The session closes by looking at how the recent wave of AI is reshaping open source security, and what the future looks like in that new..."}
```

### 11:00 AM

#### AI and attacks wipe your code and workflow in seconds. Can you recover? (Sponsored)

**Thursday, Oct 29 · 11:00 AM - 11:15 AM PDT**  
**Where:** Demos & Donuts @ Gateway Pavilion, Level 2  
**Type:** Product Demo · **Format:** In-person, AI summary

AI agents now push code at machine speed, and a single rogue agent or stolen identity can wipe a repo, overwrite history, or delete releases in seconds. And GitHub is no longer just code. It's your Issues, Actions, Projects, and Wikis, part of a broader DevOps workflow that spans Azure DevOps, Jira, and Confluence. Native controls like rulesets and immutable releases are your first line of defense, but version history isn't a backup either; it can be wiped alongside the code and pipelines it's meant to protect. This session digs into a threat most teams haven't considered and are dangerously unprepared for. Then, in a live demo, we'll recover code after an attack from the clean, isolated backups Rubrik automates. You'll leave understanding why traditional version history won't save you, and what real resilience for your entire DevOps workflow actually looks like.

**Speakers**

- Tom Bisbee: Engineering Leader, Rubrik
- Anirudh Dubey: Product Marketing (Rubrik DevOps Protection), Rubrik

```json
{"day": "2026-10-29", "start": "11:00", "end": "11:15",
 "title": "AI and attacks wipe your code and workflow in seconds. Can you recover? (Sponsored)", "room": "Demos & Donuts (Level 2)",
 "speaker": "Tom Bisbee (Rubrik), Anirudh Dubey (Rubrik)",
 "note": "This session digs into a threat most teams haven't considered and are dangerously unprepared for."}
```

#### We shipped governance: What broke, what worked, what we’d do again

**Thursday, Oct 29 · 11:00 AM - 11:15 AM PDT**  
**Where:** Ship & Tell @ Firehouse  
**Type:** Ship & Tell · **Format:** In-person, Recorded, AI summary

This team didn't plan to build a governance platform. But as the organization scaled, governance evolved from documents and approvals into logic embedded in pull requests, CI/CD pipelines, and automated checks. 

This candid Ship & Tell shows what was built, where it failed under real-world usage, and the changes that helped developers trust and adopt the platform. You’ll gain an understanding of what it takes to ship internal platforms that influence behavior, plus guidance on what does (and doesn’t) work.

**Speakers**

- Samuvel Tamilselvan Devasagayam: Principal Platform Architect, Fiserv Inc

```json
{"day": "2026-10-29", "start": "11:00", "end": "11:15",
 "title": "We shipped governance: What broke, what worked, what we'd do again", "room": "Ship & Tell",
 "speaker": "Samuvel Tamilselvan Devasagayam (Fiserv Inc)",
 "note": "This team didn't plan to build a governance platform. But as the organization scaled, governance evolved from documents and approvals..."}
```

#### AI, Actions, and tooling: Coinbase's move to GitHub with data residency

**Thursday, Oct 29 · 11:00 AM - 11:40 AM PDT**  
**Where:** Cowell Theater @ Gateway Pavilion  
**Type:** Breakout Session · **Format:** In-person, AI summary

Coinbase's rapid growth and deepening AI adoption raised the bar for its developer platform: it needed cloud scale, the latest AI capabilities, and strict compliance in a heavily regulated industry all at once. GitHub Enterprise Cloud with data residency met that bar. This session shares how Coinbase made the move.

You'll see how the team migrated 10,000+ repositories with near-zero disruption, maintaining strict compliance throughout by building a custom GitHub Actions pipeline and deploying an AI agent that drove 99% self-service across the migration. The result: developers kept shipping, and the organization stayed compliant, start to finish.

You'll leave knowing how to scale to GitHub Enterprise Cloud with data residency in a regulated environment: the tooling, the automation, and the practices that keep developers productive and compliance intact along the way.

**Speakers**

- Steven Ewing: Staff Software Engineer, Coinbase

```json
{"day": "2026-10-29", "start": "11:00", "end": "11:40",
 "title": "AI, Actions, and tooling: Coinbase's move to GitHub with data residency", "room": "Cowell Theater",
 "speaker": "Steven Ewing (Coinbase)",
 "note": "This session shares how Coinbase made the move."}
```

### 11:25 AM

#### Give GitHub Copilot more work context with Work IQ

**Thursday, Oct 29 · 11:25 AM - 11:40 AM PDT**  
**Where:** Silent Disco Demos @ Festival Pavilion  
**Type:** Product Demo · **Format:** In-person, Recorded, AI summary

GitHub Copilot can draw on your code, and Microsoft Work IQ can add relevant context from your Microsoft 365 meetings and documents. In 15 minutes, see how to connect the two and trace a requirement from a meeting transcript and design doc to its implementation.

**Speakers**

- Katie Savage: Technical Program Manager, Microsoft
- James Montemagno: Principal Technical PM Lead, Microsoft

```json
{"day": "2026-10-29", "start": "11:25", "end": "11:40",
 "title": "Give GitHub Copilot more work context with Work IQ", "room": "Silent Disco Demos",
 "speaker": "Katie Savage (Microsoft), James Montemagno (Microsoft)",
 "note": "GitHub Copilot can draw on your code, and Microsoft Work IQ can add relevant context from your Microsoft 365 meetings and documents."}
```

#### Session After Party: How GitHub secures open source

**Thursday, Oct 29 · 11:25 AM - 11:55 AM PDT**  
**Where:** The Speakeasy @ GitHub Central, Festival Pavilion  
**Type:** Session After Party · **Format:** In-person

This is an informal follow-up Q&A to the main stage session "How GitHub secures open source." Right after the talk, join Bas Alberts and Xavier René-Corail of the GitHub Security Lab in GitHub Central. Bring your questions and keep the conversation going.

**Speakers**

- Xavier René-Corail: Sr. Dir, Security Research, GitHub
- Bas Alberts: Principal Security Reseracher, GitHub

```json
{"day": "2026-10-29", "start": "11:25", "end": "11:55",
 "title": "Session After Party: How GitHub secures open source", "room": "The Speakeasy (GitHub Central)",
 "speaker": "Xavier Ren\u00e9-Corail (GitHub), Bas Alberts (GitHub)",
 "note": "This is an informal follow-up Q&A to the main stage session \"How GitHub secures open source.\" Right after the talk, join Bas Alberts and..."}
```

### 11:30 AM

#### Drowning in AI-generated vulnerability reports? Here's how to stay afloat

**Thursday, Oct 29 · 11:30 AM - 12:15 PM PDT**  
**Where:** Sandbox @ Fort Mason Building C, Founders Inc., 3rd Floor  
**Type:** Sandbox Session · **Format:** In-person

Open source maintainers are drowning in AI-generated vulnerability reports. In 2026, the volume has jumped 5x over 2025. While more scrutiny makes open source more secure in the long run, right now it's landing as a heavy burden on maintainers who are often volunteers.

This interactive session gives you a practical way to handle the flood. You'll learn how to make your SECURITY.md actually reduce noise, use the latest private vulnerability reporting features to route reports where they belong, and get interactive with prototype triage tools that GitHub Security Lab is building right now.

**Speakers**

- Kevin Stubbings: Security Researcher, GitHub
- Kevin Backhouse: Staff Manager, Security Research, GitHub

```json
{"day": "2026-10-29", "start": "11:30", "end": "12:15",
 "title": "Drowning in AI-generated vulnerability reports? Here's how to stay afloat", "room": "Sandbox, 3rd Floor",
 "speaker": "Kevin Stubbings (GitHub), Kevin Backhouse (GitHub)",
 "note": "You'll learn how to make your SECURITY.md actually reduce noise, use the latest private vulnerability reporting features to route..."}
```

#### Own your Copilot: Advanced customization for developers and platform teams

**Thursday, Oct 29 · 11:30 AM - 1:00 PM PDT**  
**Where:** Workshops @ Gateway Pavilion, Level 1  
**Type:** Workshop · **Format:** In-person

You know how to use GitHub Copilot. Now learn how to own it. This expert-level workshop breaks down every customization layer Copilot offers across app, web, and CLI. Greg Larkin and Yadhav Jayaraman walk you through eight interactive labs that build on each other. You'll leave with working artifacts, shareable templates, and a governance model for distributing customizations across your team or enterprise. No beginner basics, just practical control over how your org runs Copilot.

**Speakers**

- Yadhav Jayaraman: Staff Service Delivery Engineer, GitHub
- Greg Larkin: Senior Service Delivery Engineer, GitHub

```json
{"day": "2026-10-29", "start": "11:30", "end": "13:00",
 "title": "Own your Copilot: Advanced customization for developers and platform teams", "room": "Workshops (Level 1)",
 "speaker": "Yadhav Jayaraman (GitHub), Greg Larkin (GitHub)",
 "note": "You'll leave with working artifacts, shareable templates, and a governance model for distributing customizations across your team or..."}
```

### 11:45 AM

#### Your CI has full internet access. GitHub Actions firewall changes that.

**Thursday, Oct 29 · 11:45 AM - 12:00 PM PDT**  
**Where:** Silent Disco Demos @ Festival Pavilion  
**Type:** Product Demo · **Format:** In-person, Recorded, AI summary

Your GitHub Actions workflows have full access to the public internet. This is great for pulling dependencies. But it's a problem when you need to know exactly what your build reached out to. After an incident, can you say which URLs a workflow hit? Can you stop it from talking to anything you didn't approve?

GitHub Actions firewall sits between your workflows and the public internet. It records every outbound request, tracks which process made it, and lets you allow only the traffic you actually want, so a compromised dependency can't quietly phone home, and you have an audit trail when you need one.

In this session, you'll see how to turn it on, read the traffic it captures, and write allowlists that fit your builds.

**Speakers**

- Zach Steindler: Principal Engineer, GitHub

```json
{"day": "2026-10-29", "start": "11:45", "end": "12:00",
 "title": "Your CI has full internet access. GitHub Actions firewall changes that.", "room": "Silent Disco Demos",
 "speaker": "Zach Steindler (GitHub)",
 "note": "You'll see how to turn it on, read the traffic it captures, and write allowlists that fit your builds."}
```

### 12:00 PM

#### Copilot at scale: What 95% more pull requests taught us about measuring success

**Thursday, Oct 29 · 12:00 PM - 12:40 PM PDT**  
**Where:** Silent Disco Breakouts @ Festival Pavilion  
**Type:** Breakout Session · **Format:** In-person, AI summary

In September 2025, Precisely went all in on GitHub Copilot across engineering. A year later, pull requests are up 95%, 50% more features are delivered per quarter, and pull request merge time is down 49%. But getting to those numbers wasn’t a straight line. 

In this session, Andy Kelly and Tyler Even will walk through four challenges they encountered as adoption grew and share how to measure success as AI changes the shape of the work.

**Speakers**

- Andy Kelly: VP of Research and Development, Precisely
- Tyler Even: VP, R&D, Precisely

```json
{"day": "2026-10-29", "start": "12:00", "end": "12:40",
 "title": "Copilot at scale: What 95% more pull requests taught us about measuring success", "room": "Silent Disco Breakouts",
 "speaker": "Andy Kelly (Precisely), Tyler Even (Precisely)",
 "note": "Andy Kelly and Tyler Even will walk through four challenges they encountered as adoption grew and share how to measure success as AI..."}
```

#### The night shift: Copilot agents that maintain their own self-hosted runners

**Thursday, Oct 29 · 12:00 PM - 12:40 PM PDT**  
**Where:** BATS Theatre @ Fort Mason Building B, 3rd Floor  
**Type:** Breakout Session · **Format:** In-person, AI summary

Platform teams are being asked to do more with AI and fewer hands, but the maintenance never stops: version bumps, bug fixes, security findings, and a steady stream of vendor releases all keep coming.

Enter the second shift. This session walks through a pattern where a night shift of GitHub Copilot cloud agents maintains the same self-hosted GitHub Actions infrastructure they run on. You'll see a night in the life of that crew: agents that clock in, proactively update dependencies, read release notes and vendor blogs, open PRs, classify operational changes by risk, and auto-deploy the changes that policy already approves, escalating the rest to a human.

You'll leave with a concrete pattern for putting Copilot agents to work on your own platform maintenance: what they can safely own overnight, how to gate risky changes behind policy, and how to keep humans in control of everything that matters.

**Speakers**

- Markus Howard: Associate Director, Software Engineering, Moderna

```json
{"day": "2026-10-29", "start": "12:00", "end": "12:40",
 "title": "The night shift: Copilot agents that maintain their own self-hosted runners", "room": "BATS Theatre, 3rd Floor",
 "speaker": "Markus Howard (Moderna)",
 "note": "This session walks through a pattern where a night shift of GitHub Copilot cloud agents maintains the same self-hosted GitHub Actions..."}
```

### 12:05 PM

#### Inside Copilot's model router: How auto picks the right model for every task

**Thursday, Oct 29 · 12:05 PM - 12:20 PM PDT**  
**Where:** Silent Disco Demos @ Festival Pavilion  
**Type:** Product Demo · **Format:** In-person, Recorded, AI summary

When you use GitHub Copilot in auto mode, it routes each task to the model best suited for it, and that routing changes as the task changes. But how does it decide? Nhu Do walks through the engineering behind Copilot's auto model selection: how the routing layer evaluates task type, how it balances quality, speed, and cost across providers, and how the system continuously improves as workloads shift. You'll see a live demo of auto selection in action, learn what signals drive routing decisions under the hood, and pick up best practices for context management and planning that help auto mode work even better for you.

**Speakers**

- Nhu Do: Senior Product Manager, GitHub

```json
{"day": "2026-10-29", "start": "12:05", "end": "12:20",
 "title": "Inside Copilot's model router: How auto picks the right model for every task", "room": "Silent Disco Demos",
 "speaker": "Nhu Do (GitHub)",
 "note": "You'll see a live demo of auto selection in action, learn what signals drive routing decisions under the hood, and pick up best..."}
```

#### Inside the Lab with GitHub Next

**Thursday, Oct 29 · 12:05 PM - 12:35 PM PDT**  
**Where:** The Speakeasy @ GitHub Central, Festival Pavilion  
**Type:** Breakout Session · **Format:** In-person, AI summary

Next is constantly exploring the future shape of software development. Come by for demos of our research projects, and discussions about the themes that we believe are durably important to how we all create software.

**Speakers**

- Alex Gorischek: Senior Research Engineer, GitHub
- Maggie Appleton: Staff Research Engineer, GitHub
- David Slater: Director, Research, GitHub
- Idan Gazit: Head of GitHub Next, GitHub

```json
{"day": "2026-10-29", "start": "12:05", "end": "12:35",
 "title": "Inside the Lab with GitHub Next", "room": "The Speakeasy (GitHub Central)",
 "speaker": "Alex Gorischek (GitHub), Maggie Appleton (GitHub), David Slater (GitHub), Idan Gazit (GitHub)",
 "note": "Next is constantly exploring the future shape of software development."}
```

### 12:15 PM

#### 17 agents, one SDLC: How Levi Strauss reimagined development on GitHub

**Thursday, Oct 29 · 12:15 PM - 12:45 PM PDT**  
**Where:** Main Stage @ Festival Pavilion  
**Type:** Main Stage · **Format:** In-person, Recorded, AI summary

Levi Strauss & Co. built an enterprise multi-agent software development lifecycle on GitHub Copilot's custom agents platform. Seventeen specialized AI agents now handle requirements, spec generation, automated testing, security scanning, accessibility validation, and deployment, all connected to Jira, Confluence, and New Relic through MCP. Every pull request is reviewed by 5 to 11 independent agents that automatically fix issues and commit back to the branch, and every workflow has human approval gates built in. The result is a development lifecycle where agents do the heavy, repetitive work and people stay in control of the decisions that matter. This session shares the real story: the architecture behind the system, the lessons learned building it (including what didn't work at first), and a practical view of what a multi-agent SDLC means for enterprise teams. You'll leave understanding how the pieces fit together, where human oversight belongs, and how to think about adopting agents across your own lifecycle rather than in a single step.

**Speakers**

- Jenny Patchen: Sr. Director, Shared Platforms & Services, Levi Strauss & Co.

```json
{"day": "2026-10-29", "start": "12:15", "end": "12:45",
 "title": "17 agents, one SDLC: How Levi Strauss reimagined development on GitHub", "room": "Main Stage",
 "speaker": "Jenny Patchen (Levi Strauss & Co.)",
 "note": "This session shares the real story: the architecture behind the system, the lessons learned building it (including what didn't work at..."}
```

### 12:20 PM

#### People, process, and GitHub: Eliminating 90% of enterprise AppSec risk

**Thursday, Oct 29 · 12:20 PM - 12:35 PM PDT**  
**Where:** Ship & Tell @ Firehouse  
**Type:** Ship & Tell · **Format:** In-person, Recorded, AI summary

Application security often gets underprioritized in large enterprises, letting legacy vulnerabilities pile up under delivery pressure and a rising tide of AI-driven threats. In this session, Manulife shares how it strengthened its AppSec culture through clear communication, real-time security reporting, and GitHub-native controls.

By embedding immediate security feedback directly into GitHub, Manulife's teams remediated risk at speed and safely resolved over 90% of their vulnerabilities. You'll also see how GitHub features enable an auditable DevSecOps CI/CD pipeline that catches security and operational risks before they reach production.

You'll leave with a practical playbook for driving AppSec adoption across a large organization: the communication tactics, the real-time reporting that made risk visible, and the GitHub controls that turned a vulnerability backlog into a 90%-remediated one.

**Speakers**

- Monika Tamber: AVP, Application Security & Operational Governance, Manulife
- Benedict Mak: Director, Security Engineering, Manulife

```json
{"day": "2026-10-29", "start": "12:20", "end": "12:35",
 "title": "People, process, and GitHub: Eliminating 90% of enterprise AppSec risk", "room": "Ship & Tell",
 "speaker": "Monika Tamber (Manulife), Benedict Mak (Manulife)",
 "note": "Manulife shares how it strengthened its AppSec culture through clear communication, real-time security reporting, and GitHub-native..."}
```

### 12:25 PM

#### Plugins and engines: Extending GitHub Copilot live

**Thursday, Oct 29 · 12:25 PM - 12:40 PM PDT**  
**Where:** Silent Disco Demos @ Festival Pavilion  
**Type:** Product Demo · **Format:** In-person, Recorded, AI summary

Developers know agents exist, but many haven’t built on the agent platform themselves. In this fast-paced demo, see how a custom agent plugin is built from scratch, connected to the engine layer, and deployed to a live repository in just 15 minutes. You'll learn how plugins, skills, hooks, and MCP servers work together and know exactly how to extend the platform for your own workflows.

**Speakers**

- David O'Regan: Staff EM, GitHub

```json
{"day": "2026-10-29", "start": "12:25", "end": "12:40",
 "title": "Plugins and engines: Extending GitHub Copilot live", "room": "Silent Disco Demos",
 "speaker": "David O'Regan (GitHub)",
 "note": "You'll learn how plugins, skills, hooks, and MCP servers work together and know exactly how to extend the platform for your own workflows."}
```

### 12:45 PM

#### Make your Postgres agent-ready: Branching, isolation, and safer shipping

**Thursday, Oct 29 · 12:45 PM - 1:00 PM PDT**  
**Where:** Silent Disco Demos @ Festival Pavilion  
**Type:** Product Demo · **Format:** In-person, Recorded, AI summary

Giving agents access to real database infrastructure is risky: one wrong migration and production breaks. Database branching changes that.

When your Postgres database supports instant, isolated branches, agents can safely experiment on real schemas and data without touching production. This means safer experimentation, faster shipping, and preview environments that spin up automatically.

In this session, Andre Landgraf shows how branching and isolation work under the hood, how to set up agent-ready database environments using tools like MCP and GitHub Actions, plus a live demo of an agent managing a database branch end to end. You'll leave with a clear framework for making your own database infrastructure safe for agentic workflows.

**Speakers**

- Andre Landgraf: Staff Developer Advocate, Databricks

```json
{"day": "2026-10-29", "start": "12:45", "end": "13:00",
 "title": "Make your Postgres agent-ready: Branching, isolation, and safer shipping", "room": "Silent Disco Demos",
 "speaker": "Andre Landgraf (Databricks)",
 "note": "Andre Landgraf shows how branching and isolation work under the hood, how to set up agent-ready database environments using tools like..."}
```

#### MCP, skills, or custom agents: Picking the right tool for the job

**Thursday, Oct 29 · 12:45 PM - 1:30 PM PDT**  
**Where:** Sandbox @ Fort Mason Building C, Founders Inc., 3rd Floor  
**Type:** Sandbox Session · **Format:** In-person

GitHub Copilot gives you MCP tools, skills, and custom agents. But when do you reach for which capability? In this Sandbox session, Sam Basu runs live demos that make the differences concrete. You'll leave with a decision framework for matching the right capability to the right task, whether you're working in an IDE or a terminal.

**Speakers**

- Sam Basu: Lead Developer Advocate, Uno Platform

```json
{"day": "2026-10-29", "start": "12:45", "end": "13:30",
 "title": "MCP, skills, or custom agents: Picking the right tool for the job", "room": "Sandbox, 3rd Floor",
 "speaker": "Sam Basu (Uno Platform)",
 "note": "You'll leave with a decision framework for matching the right capability to the right task, whether you're working in an IDE or a terminal."}
```

### 12:55 PM

#### Discover, install, and manage agent skills from your terminal with gh skill

**Thursday, Oct 29 · 12:55 PM - 1:10 PM PDT**  
**Where:** Demos & Donuts @ Gateway Pavilion, Level 2  
**Type:** Product Demo · **Format:** In-person, AI summary

Agent skills make agentic workflows far more capable, but discovering, installing, and managing them across environments can be a manual, fragmented process. gh skill fixes that.

In this live demo, you’ll see the new gh skill command end to end: finding skills, installing them into your agent, and managing them, all from your terminal. Then, you’ll go under the hood on how it’s built and learn how we’re using Git primitives and agent skill frontmatter to build a smarter and more secure ecosystem.

You'll leave knowing how to add gh skill to your own workflow and what to look for in a skill before you trust it with your agent.

**Speakers**

- Tommaso Moro: Software Engineer III, GitHub

```json
{"day": "2026-10-29", "start": "12:55", "end": "13:10",
 "title": "Discover, install, and manage agent skills from your terminal with gh skill", "room": "Demos & Donuts (Level 2)",
 "speaker": "Tommaso Moro (GitHub)",
 "note": "You'll leave knowing how to add gh skill to your own workflow and what to look for in a skill before you trust it with your agent."}
```

### 1:00 PM

#### A pixel dog that writes songs: Lessons from my first MCP server

**Thursday, Oct 29 · 1:00 PM - 1:15 PM PDT**  
**Where:** Ship & Tell @ Firehouse  
**Type:** Ship & Tell · **Format:** In-person, Recorded, AI summary

It’s 2 a.m. You’re deep in a solo coding session. The terminal doesn’t care if you’re tired. Your IDE doesn’t notice you haven’t moved in an hour. But the golden retriever on your desk does. It tilts its head, nudges you with a Pomodoro timer, and when you finally ship that feature, it wags its tail and writes you a song.

Yunika Liu isn’t a backend engineer; she builds products that make complex systems feel personal. But using GitHub Copilot and its MCP support, she shipped the first version of Coco in a week. Coco is a pixel-art golden retriever that now lives in a floating desktop window and on a 64×64 LED display, powered by an MCP server with nine tools, 10 pixel animations, WebSocket sync, and music composition. In this talk, Yunika brings Coco onstage and shows how anyone can build their own MCP server. The only prerequisite is an idea weird enough to be worth building.

**Speakers**

- Yunika Liu: Product Builder, Independent

```json
{"day": "2026-10-29", "start": "13:00", "end": "13:15",
 "title": "A pixel dog that writes songs: Lessons from my first MCP server", "room": "Ship & Tell",
 "speaker": "Yunika Liu (Independent)",
 "note": "Yunika brings Coco onstage and shows how anyone can build their own MCP server."}
```

#### Session After Party: 17 agents, one SDLC: How Levi Strauss reimagined development on GitHub

**Thursday, Oct 29 · 1:00 PM - 1:30 PM PDT**  
**Where:** The Speakeasy @ GitHub Central, Festival Pavilion  
**Type:** Session After Party · **Format:** In-person

This is an informal follow-up Q&A to the main stage session "17 agents, one SDLC: How Levi Strauss reimagined development on GitHub." Right after the talk, join Jenny Patchen (Levi Strauss & Co.) in GitHub Central. Bring your questions and keep the conversation going.

**Speakers**

- Jenny Patchen: Sr. Director, Shared Platforms & Services, Levi Strauss & Co.

```json
{"day": "2026-10-29", "start": "13:00", "end": "13:30",
 "title": "Session After Party: 17 agents, one SDLC: How Levi Strauss reimagined development on GitHub", "room": "The Speakeasy (GitHub Central)",
 "speaker": "Jenny Patchen (Levi Strauss & Co.)",
 "note": "This is an informal follow-up Q&A to the main stage session \"17 agents, one SDLC: How Levi Strauss reimagined development on GitHub.\"..."}
```

#### Beyond the repository: Using a migration to rethink how you build

**Thursday, Oct 29 · 1:00 PM - 1:40 PM PDT**  
**Where:** BATS Theatre @ Fort Mason Building B, 3rd Floor  
**Type:** Breakout Session · **Format:** In-person, AI summary

Moving an engineering organization onto a new development platform is rarely just a tooling exercise. In this session, Jon Clements, DevOps and Enterprise Pipeline Manager, and Zachary Pollock, Senior Software Engineer—both at Chevron—share what the move to GitHub involved and why the work that mattered most sat outside the migration itself. You'll hear how an early-adopter community shaped the approach before the formal migration began and why sequencing let teams adopt new capabilities in stages. They also share what happened when emerging AI capabilities pushed the scope beyond development and into release, and how the team approached pipelines in GitHub Actions. Expect practical observations on change management, leadership alignment, and the importance of visibility, plus takeaways you can apply to your own migration, whether it’s finished, underway, or still being planned.

**Speakers**

- Jon Clements: DevOps & Pipeline Product Manager, Chevron
- Zachary Pollock: Sr. Software Engineer, Chevron

```json
{"day": "2026-10-29", "start": "13:00", "end": "13:40",
 "title": "Beyond the repository: Using a migration to rethink how you build", "room": "BATS Theatre, 3rd Floor",
 "speaker": "Jon Clements (Chevron), Zachary Pollock (Chevron)",
 "note": "Jon Clements, DevOps and Enterprise Pipeline Manager, and Zachary Pollock, Senior Software Engineer - both at Chevron - share what the..."}
```

#### One CLI to replace your entire JavaScript toolchain

**Thursday, Oct 29 · 1:00 PM - 1:40 PM PDT**  
**Where:** Silent Disco Breakouts @ Festival Pavilion  
**Type:** Breakout Session · **Format:** In-person, AI summary

The JavaScript ecosystem has long suffered from choice fatigue: picking a framework, deciding on a bundler, test runner, linter, and formatter, with each requiring its own setup and maintenance. 

What if one tool covered it all? Meet Vite+, the open source CLI built to manage your entire front-end toolchain, Node.js version, and package manager. 

This live demo will take you from start to finish, showing you a real migration. You'll leave knowing what Vite+ replaces today, what's coming next, and why a universal toolchain is a force multiplier when agents are writing and shipping code.

**Speakers**

- Alexander Lichter: Systems Engineer, VoidZero (Cloudflare)

```json
{"day": "2026-10-29", "start": "13:00", "end": "13:40",
 "title": "One CLI to replace your entire JavaScript toolchain", "room": "Silent Disco Breakouts",
 "speaker": "Alexander Lichter (VoidZero (Cloudflare))",
 "note": "You'll leave knowing what Vite+ replaces today, what's coming next, and why a universal toolchain is a force multiplier when agents are..."}
```

#### Treat your AI context as infrastructure

**Thursday, Oct 29 · 1:00 PM - 1:40 PM PDT**  
**Where:** Cowell Theater @ Gateway Pavilion  
**Type:** Breakout Session · **Format:** In-person, AI summary

The best way to get Copilot to write the code you want is to give it the right context. Today that means some combination of custom agents, agent skills, instructions files, MCP servers, extensions, and plugins... and the list keeps growing.

So how do you choose the right tool for the right job and get those tools into your team's hands consistently? The answer is to treat your AI context as infrastructure. This session offers practical guidance for doing exactly that: what each of these building blocks is best at, how to decide between them, and how to standardize and distribute context across your organization so every developer benefits.

You'll leave able to map the current landscape of Copilot context tools to real use cases and with a strategy for managing that context as it grows.

**Speakers**

- Christopher Harrison: Senior Developer Advocate, GitHub

```json
{"day": "2026-10-29", "start": "13:00", "end": "13:40",
 "title": "Treat your AI context as infrastructure", "room": "Cowell Theater",
 "speaker": "Christopher Harrison (GitHub)",
 "note": "This session offers practical guidance for doing exactly that: what each of these building blocks is best at, how to decide between..."}
```

### 1:05 PM

#### How we optimize GitHub Copilot for every new model.

**Thursday, Oct 29 · 1:05 PM - 1:20 PM PDT**  
**Where:** Silent Disco Demos @ Festival Pavilion  
**Type:** Product Demo · **Format:** In-person, Recorded, AI summary

How do you ship a coding agent that works brilliantly across OpenAI, Claude, Gemini, and whatever model drops next week? You build a harness. This session shares the evaluation framework the GitHub Copilot team uses to continuously test, measure, and optimize its coding agent across a matrix of clients, models, and configurations. You'll learn how the team defines reproducible benchmarks, the processes for running thousands of autonomous coding tasks, how LLM-graded assertions help catch regressions before users do, and the evaluation criteria for model integrations.

**Speakers**

- Julia Kasper: Product Manager, Microsoft

```json
{"day": "2026-10-29", "start": "13:05", "end": "13:20",
 "title": "How we optimize GitHub Copilot for every new model.", "room": "Silent Disco Demos",
 "speaker": "Julia Kasper (Microsoft)",
 "note": "This session shares the evaluation framework the GitHub Copilot team uses to continuously test, measure, and optimize its coding agent..."}
```

#### Sketching with code in the age of AI

**Thursday, Oct 29 · 1:05 PM - 1:35 PM PDT**  
**Where:** Main Stage @ Festival Pavilion  
**Type:** Main Stage · **Format:** In-person, Recorded, AI summary

AI tools can now generate clean, functional output from a short prompt. The question is no longer how to write code, but how to understand what's been made.

Qianqian Ye shows why sketching and thinking in code, beyond syntax, is essential for working with AI. Drawing from teaching creative coding at USC and leading the open source creative coding tool p5.js (built on GitHub), Qianqian demonstrates how creative coding builds the intuition to shape systems (not just prompt them) and what's lost when that iterative process disappears.

John Maeda connects the dots between design, computation, and the creative judgment that AI can't replace. You'll leave with practical approaches for integrating AI into your workflow while keeping exploration and understanding intact.

**Speakers**

- Qianqian Ye: Director of Creative Technology and Adjunct Associate Professor, Processing Foundation, University of Southern California
- John Maeda: CVP Engineering, GitHub Design and Microsoft CoreAI Design, Microsoft

```json
{"day": "2026-10-29", "start": "13:05", "end": "13:35",
 "title": "Sketching with code in the age of AI", "room": "Main Stage",
 "speaker": "Qianqian Ye (University of Southern California), John Maeda (Microsoft)",
 "note": "You'll leave with practical approaches for integrating AI into your workflow while keeping exploration and understanding intact."}
```

### 1:15 PM

#### Jev: Shipping a category-creator

**Thursday, Oct 29 · 1:15 PM - 1:30 PM PDT**  
**Where:** Demos & Donuts @ Gateway Pavilion, Level 2  
**Type:** Product Demo · **Format:** In-person, AI summary

Every new primitive faces a similar launch problem. Docker and Lambda seem obvious now, but at launch developers had to be convinced they were worth learning. Jev, the first public System One model, faces that problem twice over: it asks developers to think harder about their code just as coding agents encourage them think about it less. Allie Laabs, lead DevRel at TypeSafe, shares how Jev was shipped: the two kinds of use cases developers needed to see, the small decisions that made the idea click, and the Doom demo that showed what intelligence inside the software loop looks like.

**Speakers**

- Allie Laabs: Developer Relations, TypeSafe AI

```json
{"day": "2026-10-29", "start": "13:15", "end": "13:30",
 "title": "Jev: Shipping a category-creator", "room": "Demos & Donuts (Level 2)",
 "speaker": "Allie Laabs (TypeSafe AI)",
 "note": "Every new primitive faces a similar launch problem. Docker and Lambda seem obvious now, but at launch developers had to be convinced..."}
```

### 1:20 PM

#### Prioritization as code: Assumptions by pull request, scored by AI

**Thursday, Oct 29 · 1:20 PM - 1:35 PM PDT**  
**Where:** Ship & Tell @ Firehouse  
**Type:** Ship & Tell · **Format:** In-person, Recorded, AI summary

Most product prioritization lives in spreadsheets and slide decks — far from the code and the engineers doing the work. One team solved this by moving prioritization into GitHub, the tool engineers already trust. 

Rubrics, assumptions, OKRs, and every scored initiative live in Markdown, with every decision shipped through a pull request. An AI agent drafts the scores, but humans own the judgment. When an assumption changes, a GitHub Action automatically re-scores every dependent initiative. 

This session demonstrates why having a single source of truth is so important. You’ll see what they built, learn how to adopt the same pattern, and understand why pull request reviews proved to be a more effective forum for prioritization than any meeting.

**Speakers**

- Mina Tawadrous: Associate Director, Product Management, SiriusXM

```json
{"day": "2026-10-29", "start": "13:20", "end": "13:35",
 "title": "Prioritization as code: Assumptions by pull request, scored by AI", "room": "Ship & Tell",
 "speaker": "Mina Tawadrous (SiriusXM)",
 "note": "This session demonstrates why having a single source of truth is so important."}
```

### 2:00 PM

#### Watch the Keynote from Cowell Theater

**Thursday, Oct 29 · 2:00 PM - 2:45 PM PDT**  
**Where:** Cowell Theater @ Gateway Pavilion  
**Type:** Special Event

The full keynote streams live in Cowell Theater. If you’d like a quieter place to take it in or just want a comfortable seat with a great view of the screen, this is your spot. Same keynote, same start time, your choice of setting.

```json
{"day": "2026-10-29", "start": "14:00", "end": "14:45",
 "title": "Watch the Keynote from Cowell Theater", "room": "Cowell Theater",
 "speaker": "",
 "note": "The full keynote streams live in Cowell Theater. If you'd like a quieter place to take it in or just want a comfortable seat with a..."}
```

#### Watch the Keynote from the Outdoor Theater

**Thursday, Oct 29 · 2:00 PM - 2:45 PM PDT**  
**Where:** Outdoor Theater @ Gateway Plaza  
**Type:** Special Event · **Format:** In-person

The full keynote streams live here under the tent. Whether you want a bit of fresh air or a more relaxed way to take it all in, grab a spot and settle in. Same keynote, same start time, your choice of setting.

```json
{"day": "2026-10-29", "start": "14:00", "end": "14:45",
 "title": "Watch the Keynote from the Outdoor Theater", "room": "Outdoor Theater",
 "speaker": "",
 "note": "The full keynote streams live here under the tent. Whether you want a bit of fresh air or a more relaxed way to take it all in, grab a..."}
```

#### Closing Keynote

**Thursday, Oct 29 · 2:00 PM - 3:00 PM PDT**  
**Where:** Main Stage @ Festival Pavilion  
**Type:** Keynote · **Format:** In-person, Recorded, Livestream, AI summary

We're ending Universe the way it started: with the people who build in the open. Join us for a final session of open source voices, unexpected demos, and the kind of nerdy joy that reminds you why you got into this in the first place. More details coming soon.

**Speakers**

- Martin Woodward: VP, Developer Relations, GitHub
- Maggie Appleton: Staff Research Engineer, GitHub
- Jocelyn Velarde: GitHub Campus Expert, Tec de Monterrey

```json
{"day": "2026-10-29", "start": "14:00", "end": "15:00",
 "title": "Closing Keynote", "room": "Main Stage",
 "speaker": "Martin Woodward (GitHub), Maggie Appleton (GitHub), Jocelyn Velarde (Tec de Monterrey)",
 "note": "Join us for a final session of open source voices, unexpected demos, and the kind of nerdy joy that reminds you why you got into this in..."}
```

### 5:00 PM

#### Tonga Room & Hurricane Bar Conference Cool Down Happy Hour

**Thursday, Oct 29 · 5:00 PM - 10:00 PM PDT**  
**Where:** Tonga Room & Hurricane Bar @ Fairmont Hotel, 950 Mason St  
**Type:** Social

Join Andela after two event-filled days at GitHub Universe for a tiki-themed evening at San Francisco’s iconic Tonga Room & Hurricane Bar. Unwind with live music from the floating stage, experience the venue’s signature indoor tropical storms, and celebrate the end of an unforgettable week. Gather with fellow technology leaders over signature drinks and hors d’oeuvres, hang with colleagues, and make new connections at this unique San Francisco destination. Space is limited.

Hosted by Andela. Advance registration required .

```json
{"day": "2026-10-29", "start": "17:00", "end": "22:00",
 "title": "Tonga Room & Hurricane Bar Conference Cool Down Happy Hour", "room": "Tonga Room & Hurricane Bar",
 "speaker": "",
 "note": "Join Andela after two event-filled days at GitHub Universe for a tiki-themed evening at San Francisco's iconic Tonga Room & Hurricane Bar."}
```

### 6:00 PM

#### Figma Developer Meetup

**Thursday, Oct 29 · 6:00 PM - 9:00 PM PDT**  
**Where:** Figma HQ @ 760 Market St  
**Type:** Social

Join us at the Figma SF office for an evening with the teams working on Figma developer tools and Payload. Come for the food and drinks, stay for the conversations. Lightning talks and open discussions around: - How Figma’s MCP server and Code Connect help agents understand design intent and generate code with real production components - How developers can align on what to build and visualize their codebase in agentic workflows - How Payload’s open-source, AI-native content framework works with the Figma ecosystem Who should come - Front end, full stack, and platform developers. Design systems engineers. Anyone working with coding agents day to day.

Hosted by Figma. Advance registration required .

```json
{"day": "2026-10-29", "start": "18:00", "end": "21:00",
 "title": "Figma Developer Meetup", "room": "Figma HQ",
 "speaker": "",
 "note": "Join us at the Figma SF office for an evening with the teams working on Figma developer tools and Payload."}
```
