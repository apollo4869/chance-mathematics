"""Bilingual landing pages; chapter manuscripts remain the sole content source."""
import html
import re

EN_TITLES = [
    'An Unfinished Game',
    'From Chance to Knowledge: Learning an Unknown Probability',
    'The Birth of the Bell Curve',
    'Randomness Enters Time: From Random Walks to Brownian Motion',
    'The Price of Infinity: Why Probability Needs Measure Theory',
    'The Rebirth of the Mean: From Weighted Sums to Lebesgue Integration',
    'What Does Convergence Mean? Four Limits in a Random World',
    'How Can We Construct an Infinite Random Experiment?',
    'After Seeing Part of the World: Conditional Expectation and Information',
    'How Can One Probability Be Decomposed in Terms of Another? Densities, Conditional Laws and Kernels',
    'How Can a Distribution Be Recorded by a Function? Characteristic Functions, Independent Sums and Gaussian Limits',
]
EN_TITLES.append('When Can Infinitely Many Additions Still Have an Answer?')
EN_TITLES.append('Why Do Rare Events Produce New Stable Laws?')
EN_TITLES.append('Not Every Limit Is Gaussian—Triangular Arrays, Stable Laws and Infinite Divisibility')
EN_TITLES.append('What Becomes of a Game That Remains Fair Forever?')
EN_TITLES.extend(['What If the Player Chooses When to Stop?','Does the Present Suffice to Determine the Future?','Why Do Some Random Walks Return While Others Escape?','Waiting for a New Beginning','How Does One Ancestor Become a Random Family?'])
EN_DESCRIPTIONS = [
    'Fairness, symmetry, independence and additivity, beginning with an interrupted game.',
    'Frequencies, Bernoulli, Bayes and the problem of inference.',
    'de Moivre, Laplace, Gauss and the emergence of Gaussian limits.',
    'Square-root scaling, joint distributions, covariance and the question of a random path.',
    'From the difficulties of infinite sets to sigma-algebras, outer measures and probability.',
    'Integration, expectation and the conditions for exchanging a limit with an integral.',
    'Rare recurring events, moving windows, spikes and uniform integrability.',
    'Consistent finite-dimensional rules, measure extension and a common space of records.',
    'Fair prices, observable information, orthogonal prediction and Bayesian updating.',
    'Densities, singular mass, regular conditional laws, disintegration and sequential experiments.',
    'Bounded frequency readings, inversion, Lévy continuity and a complete finite-variance central limit proof.',
]
EN_DESCRIPTIONS.append('First crossings, independent series, three-series criteria, integrable strong laws and tail information.')
EN_DESCRIPTIONS.append('Rare counts, Le Cam coupling, independent marks, Laplace transforms and the lattice local central limit theorem.')
EN_DESCRIPTIONS.append('Changing independent rows, Lindeberg–Feller, multivariate limits, stable attraction and infinite divisibility.')
EN_DESCRIPTIONS.append('Fair capital, maximal and crossing estimates, closed martingales, Lp convergence and decreasing information.')
EN_TITLES.append('Waiting without Memory—The Poisson Process')
STAR = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="m12 2.8 2.8 5.7 6.3.9-4.6 4.5 1.1 6.3-5.6-3-5.6 3 1.1-6.3L2.9 9.4l6.3-.9Z"/></svg>'


EN_DESCRIPTIONS.extend(['Stopping rules, bounded sampling, UI settlement and gambling counterexamples.','Markov kernels, sequential construction, strong Markov and stationary structure.','Returns, Green functions and the dimensional fate of random walks.','Renewal equations, key renewal, length bias and stationary waiting.','Extinction, population martingales, spines and the x log x condition.'])

EN_DESCRIPTIONS.append('Exponential waits, counting paths, independent windows, compensated martingales and split or merged streams.')

EN_TITLES.append('How Can a Random Process Jump?—Continuous-Time Markov Chains')
EN_DESCRIPTIONS.append('State-dependent clocks, minimal jump chains, explosion, Kolmogorov equations, invariant laws and timed branching.')

EN_TITLES.append('How Can Gaussian Snapshots Become Continuous Paths?—Continuous Modifications, Gaussian Processes and Wiener Measure')
EN_DESCRIPTIONS.append('Gaussian covariance, countable-grid continuity, Wiener measure, bridges, Ornstein–Uhlenbeck motion and isonormal geometry.')

EN_TITLES.append('How Can an Entire Random Path Converge?—Portmanteau, Prokhorov and Function-Space Topologies')
EN_DESCRIPTIONS.append('From missed spikes to Polish weak limits, coupling, continuous-path tightness and jump-time alignment.')

EN_TITLES.append('When Does a Random Walk Become Brownian Motion?—Donsker’s Invariance Principle')
EN_TITLES.append('Why Is a Continuous Path So Rough?')
EN_DESCRIPTIONS.append('Finite-variance path limits through fixed truncation, maximal estimates, empirical bridges and inverse renewal clocks.')
EN_DESCRIPTIONS.append('From first-hit reflection to nowhere differentiability, exact oscillation, functional LIL and arcsine occupation laws.')
EN_TITLES.append('What If Random Motion Jumps as Well as Diffuses?—Lévy Processes and Lévy–Khintchine Theory')
EN_DESCRIPTIONS.append('Compensated small jumps, Lévy triplets, original-space decomposition, stable attraction and jump limits.')

EN_TITLES.append('Why Does Random Motion Produce Deterministic Equations? Semigroups, Generators and Resolvents')
EN_DESCRIPTIONS.append('Expected observations, generator domains, discounted occupation, Yosida construction and regular Markov paths.')
EN_TITLES.append('When Small Probabilities Become Exponentially Small—Large Deviations')
EN_DESCRIPTIONS.append('From all-heads records to exponential tilting, entropy, empirical measures and squared Brownian path energy.')
EN_TITLES.append('What Does It Mean to Know Before It Happens?')
EN_DESCRIPTIONS.append('Newly observed arrivals, optional and predictable information, regularization, Doob–Meyer and finite-variation compensation.')
EN_TITLES.append('How Can We Integrate Along a Nondifferentiable Random Path?—Itô Integral and Quadratic Variation')
EN_DESCRIPTIONS.append('Left sums and surviving squares, Itô isometry, predictable L2 extension, continuous martingale brackets and random energy clocks.')
EN_TITLES.append('Why Must the Familiar Calculus Change?—Itô Formula, Stratonovich and Initial SDEs')
EN_DESCRIPTIONS.append('Cubic remainders lead to Itô formula, symmetric integration and clocks, with actual constructions of linear stochastic equations.')
EN_TITLES.append('The Deeper Relations Between Brownian Motion and Martingales')
EN_DESCRIPTIONS.append('Probability weights, quadratic clocks and information: measure change, DDS, natural-filtration representation and stopping-time embedding.')
EN_TITLES.append('When Continuous Motion and Jumps Appear Together')
EN_DESCRIPTIONS.append('A non-negligible jump leads to semimartingale integration, compensation, jump Itô and limit tools.')

def repository_url(config):
    repo = config.get('github_repository')
    if not repo:
        return None
    if not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repo):
        raise ValueError('github_repository must be a confirmed owner/repository or null')
    return 'https://github.com/' + repo


def utility(config, english=False, counterpart=None):
    repo = repository_url(config)
    github = ('<a href="'+html.escape(repo)+'" target="_blank" rel="noopener noreferrer">GitHub ↗</a>' if repo else
              '<span class="unavailable" aria-disabled="true">GitHub<small>'+('not yet available' if english else '待开放')+'</small></span>')
    return ('<nav class="site-utility" aria-label="'+('Book links' if english else '全书入口')+'">'
            '<a href="'+('/en/index.html#contents' if english else '/index.html#contents')+'">'+('Contents' if english else '全书目录')+'</a>'
            + github + '<a data-language-switch href="'+(counterpart or ('/index.html' if english else '/en/index.html'))+'" lang="'+('zh-CN' if english else 'en')+'">'+('中文' if english else 'English')+'</a></nav>')


def hero(config, count, english=False):
    repo = repository_url(config)
    star_inner = STAR + '<span>Star on GitHub</span>'
    if repo:
        star = '<a class="github-star" href="'+html.escape(repo)+'" target="_blank" rel="noopener noreferrer">'+star_inner+'<span aria-hidden="true">↗</span></a>'
    else:
        star = ('<span class="github-star" role="link" aria-disabled="true">'+star_inner+
                '<span class="repository-state">'+('Not yet available' if english else '仓库待开放')+'</span></span>')
    if english:
        title = 'The Mathematics<br>of Chance'
        subtitle = 'The history, ideas and mathematical<br>structures of probability'
        eyebrow = 'AN ORIGINAL BOOK ON PROBABILITY'
        secondary_title = '偶然的数学'
        intro = ('From an interrupted game to random paths: follow the problems that made new mathematical ideas necessary, '
                 'with sustained arguments, counterexamples and proofs.')
        status = f'{count} long-form chapters · Work in progress'
        start, contents = 'Start reading', 'Explore the contents'
        downloads = ('<a href="/downloads/complete-offline.zip" download>Offline bilingual edition ↓</a>'
                     '<a href="/downloads/english-manuscript.zip" download>English manuscripts ↓</a>')
        language_note = f'<p class="language-note">Complete English translations of all {count} chapters and their proof materials. A working translation for author review, with the Chinese manuscripts preserved independently.</p>'
        community_note = 'Follow the project when its repository becomes available.' if not repo else 'Read the source and follow the book on GitHub.'
        cover_alt = 'The Mathematics of Chance, book cover'
    else:
        title = '偶然的数学'
        subtitle = '概率论的历史、思想与数学结构'
        eyebrow = '从真实问题走向现代概率论'
        secondary_title = 'THE MATHEMATICS OF CHANCE'
        intro = '从一场没有结束的赌博，到一条尚待构造的随机路径。沿着真实的数学问题，理解概念为何产生，发现随机世界背后的数学结构。'
        status = f'{count}章长篇工作稿 · 持续写作中'
        start, contents = '开始阅读', '浏览全书目录'
        downloads = ('<a href="/downloads/complete-offline.zip" download>下载离线版 ↓</a>'
                     '<a href="/downloads/editable-manuscript.zip" download>可编辑原稿 ↓</a>')
        language_note = ''
        community_note = 'GitHub 仓库开放后，可在这里关注本书。' if not repo else '在 GitHub 阅读源码、关注本书的后续更新。'
        cover_alt = '偶然的数学：概率论的历史、思想与数学结构，书籍封面'
    return ('<section id="cover" class="home-hero" aria-labelledby="book-title">'
            '<figure class="home-book"><img src="/assets/ui/book-cover.svg" width="400" height="540" alt="'+cover_alt+'"></figure>'
            '<div class="hero-copy"><div class="hero-title-block"><div class="eyebrow">'+eyebrow+'</div>'
            '<h1 id="book-title">'+title+'</h1><p class="hero-subtitle">'+subtitle+'</p>'
            '<p class="hero-english-title">'+secondary_title+'</p><p class="hero-author">'+('By ' if english else '作者：')+'<a href="'+('/en' if english else '')+'/author.html">Haobai Wang</a></p></div><div class="hero-reading-block">'
            '<p class="hero-intro">'+intro+'</p><p class="hero-status">'+status+'</p>'
            '<div class="hero-actions"><a class="primary" href="'+('/en' if english else '')+'/volumes/01-opening.html">'+start+' <span>→</span></a>'
            '<a class="secondary" href="#contents">'+contents+'</a><button id="resume" hidden>'+('Resume reading' if english else '继续上次阅读')+'</button></div>'
            '<div class="hero-resources">'+downloads+'</div><div class="hero-community">'+star+
            '<span class="hero-community-note">'+community_note+'</span></div>'+language_note+'</div></div></section>')


def english_catalogue(slugs):
    result = '<section class="catalogue" id="contents"><h2>Read the book</h2><p class="section-search-hint">Each chapter opens its complete English text. Switch between section and full-chapter reading at any time.</p>'
    for i, slug in enumerate(slugs):
        title = EN_TITLES[i]
        result += ('<a class="catalogue-item" href="/en/chapters/'+slug+'.html"><span class="chapter-number">'+f'{i+1:02}'+'</span>'
                   '<span><span class="catalogue-title">'+html.escape(title)+'</span><span class="catalogue-description">'+html.escape(EN_DESCRIPTIONS[i])+'</span></span>'
                   '<span class="catalogue-arrow" aria-hidden="true">→</span></a>')
    result += ('<div class="extra-pages"><a href="/en/reading-routes.html">Further reading &amp; proof routes</a>'
               '<a href="/en/references.html">References</a><a href="/en/writing-rules.html">Writing principles</a></div></section>')
    return result


def english_sidebar(slugs):
    return ('<aside id="sidebar"><div class="side-label">CONTENTS</div><a class="catalogue-home" href="/en/index.html">← Book home</a>'
            '<nav>' + ''.join('<a class="toc-sub" href="/en/chapters/'+slug+'.html">'+str(i+1)+'. '+html.escape(EN_TITLES[i])+'</a>' for i, slug in enumerate(slugs)) +
            '</nav><a class="aside-end" href="/en/reading-routes.html">Further reading and proofs</a></aside>')

EN_TITLES.append('Does a Stochastic Differential Equation Have a Solution?')
EN_DESCRIPTIONS.append('Rules, existing processes and uniqueness: construction, causal kernels, martingale problems and feedback limits.')

EN_TITLES.append('What Determines the Fate of a One-Dimensional Diffusion?')
EN_DESCRIPTIONS.append('Scale reads hitting chances; speed reads occupation time, boundaries and long-term fate.')

EN_TITLES.append('How Much Has a Path Accumulated at One Position?')
EN_DESCRIPTIONS.append('Local time, occupation, Poisson excursions and spatial branching; singular speed and boundary clocks.')

EN_TITLES.append('Random Motion Meets Partial Differential Equations Again')
EN_DESCRIPTIONS.append('Feynman–Kac, boundary regularity, Green potentials, capacity, sweeping and precisely scoped Revuz correspondence.')

EN_TITLES.append('How Can We Differentiate Randomness?')
EN_DESCRIPTIONS.append('Gaussian noise sensitivity, closed derivatives, chaos, density criteria and predictable representation.')

EN_TITLES.append('When Random Paths Enter Curved Space')
EN_DESCRIPTIONS.append('Coordinate compatibility, Riemannian Brownian motion, development and geometric lifetime.')

EN_TITLES.append('Why Can a Random World Exhibit Long-Term Stability?')
EN_DESCRIPTIONS.append('Invariant information, random conditional averages, ergodic limits, subadditivity and information rates.')

EN_TITLES.append('When Does a Random System Forget Its Initial State?')
EN_DESCRIPTIONS.append('Common mass, split cycles, Harris recurrence, synchronized clocks, total variation and ratio limits.')

EN_TITLES.append('If We Reorder Observations, Does Probability Stay the Same?')
EN_DESCRIPTIONS.append('Finite symmetry, reverse martingales, directing probabilities, conditional iid representation and learning from records.')

EN_TITLES.append('Why Do Dependent Samples Look Like Repeated Predictions?')
EN_DESCRIPTIONS.append('Order-consistent reinforcement, Dirichlet random probabilities, posterior kernels, stick weights and exchangeable tables.')

EN_TITLES.append('What Does Symmetry Actually Preserve?')
EN_DESCRIPTIONS.append('Haar averaging, orbit conditioning, modular factors, predictable sampling and rotational Gaussian mixtures.')

EN_TITLES.append('When Exchangeable Objects No Longer Form a Sequence')
EN_DESCRIPTIONS.append('Shared-index information, Aldous–Hoover representations, dissociation and nonunique graphon coordinates.')

EN_TITLES.append('How Do Random Partitions Grow, Merge and Evolve?')
EN_DESCRIPTIONS.append('Paintbox masses and dust, Ewens sampling, consistent Kingman paths and mutation.')

EN_TITLES.append('When a Random Outcome Is a Collection of Points')
EN_DESCRIPTIONS.append('Point measures, Laplace identification, spatial Poisson and Cox models, marking and limits.')

EN_TITLES.append('When a Random Outcome Is a Measure')
EN_DESCRIPTIONS.append('Random Radon mass, vague and weak limits, smoothing, dissipative scattering, Cox and cluster structures.')

EN_TITLES.append('What Do We See from a Typical Random Point?')
EN_DESCRIPTIONS.append('Sampling occurrences, Campbell disintegration, Palm inversion, Mecke identification, and Gibbs kernels.')

EN_TITLES.append('How Can a Random Set Have a Probability Law?')
EN_DESCRIPTIONS.append('Closed shapes, hit-or-miss topology, Choquet representation, and capacity convergence.')

EN_TITLES.append('From Family Genealogies to Random Trees')
EN_DESCRIPTIONS.append('Invertible tree encodings, indexed cyclic cuts, and exact Galton–Watson total-size laws.')

EN_TITLES.append('Why Do Discrete Random Trees Develop Continuous Shapes?')
EN_DESCRIPTIONS.append('Conditioned bridges, Vervaat cuts, and finite-variance joint limits for tree height and contour.')

EN_TITLES.append('How Does a Brownian Excursion Become a Tree?')
EN_DESCRIPTIONS.append('Excursion quotients, unique arcs, sampling mass and the exact laws of reduced CRT subtrees.')

EN_TITLES.append('How Can Two Random Geometric Spaces Be Close?')
EN_DESCRIPTIONS.append('Correspondences, mass couplings, Polish geometry and the rooted GHP limit of conditioned family trees.')

EN_TITLES.append('How Can Random Structures Split, Merge and Remain Consistent?')
EN_DESCRIPTIONS.append('Sampling consistency, nested hierarchies, dislocations, self-similar clocks, dust and geometric cuts.')

EN_TITLES.append('How Does a Tree Form Through Random Growth?')
EN_DESCRIPTIONS.append('Consistent branching, spinal sampling, CRP growth and a complete standard-scale Brownian line-breaking construction.')

EN_TITLES.append('From Binary Trees to Multifurcating Random Geometry')
EN_DESCRIPTIONS.append('Fixed-k Brownian universality, published growth models, mass splits, compact Levy forests and ICRT hubs, with explicit proof boundaries.')
