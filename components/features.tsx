import { Card, CardContent } from "@/components/ui/card"
import { Zap, Shield, Globe, Users } from "lucide-react"

const features = [
  {
    icon: Zap,
    title: "Real-Time Translation",
    description:
      "Instant sign language recognition and text conversion with advanced AI models trained on diverse datasets.",
  },
  {
    icon: Shield,
    title: "Privacy First",
    description: "Your data stays secure. All processing happens locally and no permanent storage.",
  },
  {
    icon: Globe,
    title: "Lightweight but Efficient",
    description: "A lightweight but efficient software that ensures minimal latency and high accuracy",
  },
  {
    icon: Users,
    title: "Inclusive Design",
    description: "Built with accessibility at the core, ensuring usability for everyone regardless of ability.",
  },
]

export function Features() {
  return (
    <section id="features" className="py-24 sm:py-28 lg:py-36 bg-muted/40">
      <div className="container mx-auto px-4 sm:px-6 lg:px-8">
        <div className="max-w-2xl mx-auto text-center mb-20">
          <h2 className="text-3xl sm:text-4xl lg:text-5xl font-bold text-foreground text-balance mb-5 tracking-tight">
            Empowering Communication
          </h2>
          <p className="text-lg text-muted-foreground text-pretty leading-relaxed">
            Technology designed to bridge communication gaps and create inclusive experiences.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          {features.map((feature, index) => {
            const Icon = feature.icon
            return (
              <Card
                key={index}
                className="border border-border bg-card hover:shadow-xl hover:border-accent/30 transition-all duration-300 group"
              >
                <CardContent className="pt-8 pb-6 px-6">
                  <div className="flex items-center justify-center w-14 h-14 rounded-xl bg-gradient-to-br from-accent/20 to-secondary/20 mb-6 group-hover:scale-110 transition-transform duration-300">
                    <Icon className="w-7 h-7 text-accent" aria-hidden="true" />
                  </div>
                  <h3 className="text-xl font-semibold text-card-foreground mb-3 tracking-tight">{feature.title}</h3>
                  <p className="text-muted-foreground leading-relaxed text-[15px]">{feature.description}</p>
                </CardContent>
              </Card>
            )
          })}
        </div>
      </div>
    </section>
  )
}
