import { Card, CardContent } from "@/components/ui/card"

const steps = [
  {
    number: "1",
    title: "Capture",
    description: "Use your camera to record sign language gestures in real-time or upload pre-recorded videos.",
  },
  {
    number: "2",
    title: "Analyze",
    description: "Our AI model processes hand movements, facial expressions, and body language with precision.",
  },
  {
    number: "3",
    title: "Translate",
    description: "Receive instant text translation with context-aware accuracy and natural language output.",
  },
]

export function HowItWorks() {
  return (
    <section id="how-it-works" className="py-24 sm:py-28 lg:py-36">
      <div className="container mx-auto px-4 sm:px-6 lg:px-8">
        <div className="max-w-2xl mx-auto text-center mb-20">
          <h2 className="text-3xl sm:text-4xl lg:text-5xl font-bold text-foreground text-balance mb-5 tracking-tight">
            How It Works
          </h2>
          <p className="text-lg text-muted-foreground text-pretty leading-relaxed">
            Three simple steps to seamless communication
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-6xl mx-auto">
          {steps.map((step, index) => (
            <div key={index} className="relative">
              <Card className="border border-border bg-card h-full hover:shadow-xl hover:border-accent/30 transition-all duration-300 group">
                <CardContent className="pt-10 pb-8 px-6">
                  <div className="flex items-center justify-center w-20 h-20 rounded-2xl bg-gradient-to-br from-primary to-secondary text-primary-foreground text-3xl font-bold mb-6 mx-auto shadow-lg group-hover:scale-110 transition-transform duration-300">
                    {step.number}
                  </div>
                  <h3 className="text-2xl font-semibold text-card-foreground mb-4 text-center tracking-tight">
                    {step.title}
                  </h3>
                  <p className="text-muted-foreground leading-relaxed text-center text-[15px]">{step.description}</p>
                </CardContent>
              </Card>
              {index < steps.length - 1 && (
                <div
                  className="hidden md:block absolute top-1/2 -right-4 w-8 h-0.5 bg-gradient-to-r from-border to-transparent"
                  aria-hidden="true"
                />
              )}
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}
