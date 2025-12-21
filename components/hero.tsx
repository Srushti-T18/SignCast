import { Button } from "@/components/ui/button"
import { ArrowRight, Video } from "lucide-react"

export function Hero() {
  return (
    <section className="relative pt-36 pb-24 sm:pt-44 sm:pb-28 lg:pt-56 lg:pb-36 overflow-hidden">
      <div
        className="absolute inset-0 bg-gradient-to-b from-accent/5 via-transparent to-transparent pointer-events-none"
        aria-hidden="true"
      />

      <div className="container mx-auto px-4 sm:px-6 lg:px-8 relative">
        <div className="max-w-4xl mx-auto text-center">
          <h1 className="text-4xl sm:text-5xl lg:text-7xl font-bold text-foreground text-balance leading-[1.1] mb-7 tracking-tight">
            Breaking Barriers with{" "}
            <span className="bg-gradient-to-r from-accent to-secondary bg-clip-text text-transparent">AI-Powered</span>{" "}
            Sign Language Translation
          </h1>
          <p className="text-lg sm:text-xl text-muted-foreground text-pretty max-w-2xl mx-auto mb-12 leading-relaxed">
            Transform sign language into text instantly. Our accessibility-first platform empowers communication for
            everyone, anywhere.
          </p>

          <div className="flex flex-col sm:flex-row items-center justify-center gap-4 mb-20">
            <Button
              size="lg"
              className="w-full sm:w-auto group bg-gradient-to-r from-primary to-secondary hover:shadow-xl transition-all duration-300 px-8 py-6 text-base"
            >
              Start Translating
              <ArrowRight className="ml-2 h-5 w-5 transition-transform group-hover:translate-x-1" aria-hidden="true" />
            </Button>
            <Button
              size="lg"
              variant="outline"
              className="w-full sm:w-auto border-2 hover:bg-muted/50 transition-all duration-200 px-8 py-6 text-base bg-transparent"
            >
              <Video className="mr-2 h-5 w-5" aria-hidden="true" />
              Watch Demo
            </Button>
          </div>

          <div className="relative aspect-video rounded-2xl overflow-hidden border-2 border-border shadow-2xl bg-muted ring-1 ring-black/5">
            <img
              src="/person-using-sign-language-with-ai-translation-int.jpg"
              alt="Person using sign language with AI translation interface overlay"
              className="w-full h-full object-cover"
            />
          </div>
        </div>
      </div>
    </section>
  )
}
