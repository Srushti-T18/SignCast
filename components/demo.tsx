import { Card, CardContent } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Play } from "lucide-react"

export function Demo() {
  return (
    <section
      id="demo"
      className="py-24 sm:py-28 lg:py-36 bg-gradient-to-br from-primary via-primary to-secondary text-primary-foreground relative overflow-hidden"
    >
      <div
        className="absolute inset-0 bg-[radial-gradient(circle_at_30%_50%,rgba(255,255,255,0.1),transparent_50%)] pointer-events-none"
        aria-hidden="true"
      />

      <div className="container mx-auto px-4 sm:px-6 lg:px-8 relative">
        <div className="max-w-6xl mx-auto">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
            <div>
              <h2 className="text-3xl sm:text-4xl lg:text-5xl font-bold text-balance mb-7 tracking-tight">
                See SignCast in Action
              </h2>
              <p className="text-lg text-primary-foreground/95 leading-relaxed mb-10 text-pretty">
                Experience the power of real-time sign language translation. Watch how our technology creates instant,
                accurate text from sign language gestures.
              </p>
              <Button
                size="lg"
                variant="secondary"
                className="group shadow-xl hover:shadow-2xl transition-all duration-300 px-8 py-6 text-base"
              >
                <Play className="mr-2 h-5 w-5 transition-transform group-hover:scale-110" aria-hidden="true" />
                Play Demo Video
              </Button>
            </div>

            <Card className="border-2 border-primary-foreground/20 bg-primary-foreground/10 backdrop-blur-sm shadow-2xl">
              <CardContent className="p-0">
                <div className="relative aspect-video rounded-xl overflow-hidden bg-primary-foreground/10 ring-1 ring-primary-foreground/20">
                  <img
                    src="/sign-language-translation-demo-interface.jpg"
                    alt="Sign language translation demo interface showing real-time conversion"
                    className="w-full h-full object-cover"
                  />
                  <div className="absolute inset-0 flex items-center justify-center">
                    <Button
                      size="lg"
                      variant="secondary"
                      className="rounded-full w-20 h-20 p-0 shadow-2xl hover:scale-110 transition-transform duration-300"
                    >
                      <Play className="h-7 w-7 ml-1" aria-hidden="true" />
                      <span className="sr-only">Play video</span>
                    </Button>
                  </div>
                </div>
              </CardContent>
            </Card>
          </div>
        </div>
      </div>
    </section>
  )
}
