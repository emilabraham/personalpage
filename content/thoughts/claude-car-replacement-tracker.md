---
title: "Claude Project: Car Replacement Mileage Tracker"
publishDate: 2026-01-27T00:00:00-07:00
---

## The Overview

I recently moved to a new place in Mountain View, California.
My grocery store is 1 mile away. My gym is 3 miles away.
Too far to walk regularly, but perfect for a bicycle.

With year-round great weather and no commute, I decided to try going car-lite.
But I wanted to know: is this actually saving me money? How much driving am I really avoiding?

To find out, I needed to track every trip where I chose my bike or public transit over my car.

## The Problem

I want to track how many miles I am saving on my car by deciding to ride by bike or take public transit.
What if I just track my mileage on my bike?
Or just turn on Google Maps trip tracking?
I know that it can often differentiate between modes of transportation.
There are a few problems with this:

- The miles are not one-to-one.
Sometimes the bicycle route is far less direct than the car route.
Sometimes the car route is far less direct than the bicycle route.
- Google Maps automatic tracking is okay. But not good enough for this use case.
- Not every trip I take with my bike or walk, is a car replacement trip.
For example, I don't think I'll ever take my car downtown.
It's only a 15 minute walk away. This would lead to some false-positives in Google Maps.

## Brainstorming

Before reaching for AI, I thought about how I'd build this myself. I started by laying out requirements.

### Requirements

- Specify start and end locations, then calculate the driving distance between them. This probably means some kind of map UI with support for round trips and multi-stop routes.
- Store the data somewhere. A CSV file would work. The main goal is just summing total mileage.
- Edit past trips in case I log something wrong.
- View previous trips and see cumulative mileage saved.

### Nice to haves

- Log trips from my phone.

## Why an AI Solution?

Before building anything, I considered two approaches: have Claude do it, or build a standalone app.

A standalone app would be shareable and predictable. Same input, same output every time.
But I'd have to relearn mapping APIs, decide between a mobile app or web app, and handle a bunch of unknowns before writing any real logic.

The AI approach flips this.
I can describe what I want in plain English: "log a round trip to Safeway."
No UI to build, no map widgets to wrangle.
The core task is simple: call an API, calculate a distance, save it to a file. So why over-engineer it?

The tradeoff is that AI isn't perfectly predictable.
Given the same input, it might phrase things differently or occasionally misinterpret instructions.
And there's nothing impressive to show off at the end. Just a spreadsheet and some scripts.

But here's what sold me: choosing the AI approach doesn't close any doors.
If I outgrow it, I can take everything I've learned and build the standalone app later.
Or I might just be happy with what I have.

## My Solution

### Building It

I started by asking Claude to find a free geocoding API, something that could turn "Safeway" into GPS coordinates.
It found one, we tested it, and wrapped it in a reusable script.

Next, I needed driving distances between two coordinates.
Claude found another free API for that. Same process: test it, wrap it in a script.

Finally, I asked Claude to create an agent that ties everything together.
Give it a destination, and it looks up the coordinates, calculates the driving distance, and logs it to a CSV.

### How It Works In Practice

The result is surprisingly flexible.
I can say "Home" and it knows my address.
If I say "Safeway" and there are multiple locations, it asks me to pick one.
If I've already logged a trip before, it pulls the distance from the CSV instead of hitting the API again.

It's like having a semantic UI for free. No buttons, no dropdowns. Just plain English.

### Running It From My Phone

One of my nice-to-haves was the ability to log trips from my phone.
The solution: run Claude Code on a home server with the scripts and CSV file, then SSH in from anywhere.

I bought a small PC, installed Debian and Tailscale, and connected my phone to the same Tailscale network.
Now I can SSH into the server from my phone and talk to the agent.

My phone's keyboard has speech-to-text, so I don't even need to type.
I just speak: "log a round trip to the gym."
The agent does the work and prompts me for any clarification along the way.
It really does feel like having an assistant.

### Some Rough Edges

The agent occasionally claims it provided bicycle directions instead of driving directions.
When I check, the script is correctly set to "driving" mode. So it's a hallucination in the response, not the actual calculation.
Adding explicit instructions to the agent.md file to always use driving mode seems to have fixed this.

Logging a trip also takes longer than you'd expect.
The scripts themselves are fast, but most of the time is spent waiting for Claude to generate its responses.
Could I build a custom app that's faster?
I doubt it.
The steps to log a single trip (search for location, confirm, calculate distance, save) would take roughly the same amount of time either way.
Unless I built something that automatically tracked and categorized all my trips, Claude is probably just as fast.

### What's Next

I've been using this system for a few weeks now, and the friction is low enough that I actually use it.
The real test will be looking back after a few months to see how many miles I've avoided driving, and see how successful the car-lite experiment is.
