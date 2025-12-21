import { Button } from "@/components/ui/button"
import { ArrowRight } from "lucide-react"

export function CTA() {
  return (
    <section className="py-24 sm:py-28 lg:py-36 bg-gradient-to-b from-background to-muted/40">
      <div className="container mx-auto px-4 sm:px-6 lg:px-8">
        <div className="max-w-3xl mx-auto text-center">
          <h2 className="text-3xl sm:text-4xl lg:text-5xl font-bold text-foreground text-balance mb-10 tracking-tight">
            Ready to Transform Communication?
          </h2>
          <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
            <Button
              size="lg"
              className="w-full sm:w-auto group bg-gradient-to-r from-primary to-secondary hover:shadow-xl transition-all duration-300 px-10 py-7 text-base"
            >
              Get Started
              <ArrowRight className="ml-2 h-5 w-5 transition-transform group-hover:translate-x-1" aria-hidden="true" />
            </Button>
          </div>
        </div>
      </div>
    </section>
  )
}
