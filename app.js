document.addEventListener('DOMContentLoaded', function() {
    const isMobile = /Mobile|Android|iPhone/i.test(navigator.userAgent);
    if (!isMobile) {
        document.body.innerHTML = '<p class="mobile">Sorry, this game is only available on mobile devices.</p><img id="QRcode" src="img/qrcode_tillo09.github.io.png" alt="QRcode torcoin app">';
    } else {
        initializeGame();
    }
});

function initializeGame() {
    let coinCount = parseInt(localStorage.getItem('coinCount')) || 0;
    let energyCount = parseInt(localStorage.getItem('energyCount')) || 1000;
    const maxEnergy = 1000;
    const rechargeSteps = 1;
    const lastUpdatedKey = 'lastUpdated';

    function updateCoinCount() {
        document.getElementById('coins').textContent = coinCount.toLocaleString();
    }

    function updateEnergyCount() {
        document.getElementById('energy').textContent = energyCount;
        document.getElementById('energy-progress').style.width = `${(energyCount / maxEnergy) * 100}%`;
    }

    function collectTorCoin() {
        if (energyCount > 0) {
            coinCount++;
            energyCount = Math.max(0, energyCount - 1);
            localStorage.setItem('coinCount', coinCount.toString());
            localStorage.setItem('energyCount', energyCount.toString());
            localStorage.setItem(lastUpdatedKey, Date.now().toString());
            updateCoinCount();
            updateEnergyCount();

            console.log(`You collected 1 Torcoin! Total Torcoins: ${coinCount}`);
            console.log(`Energy remaining: ${energyCount}%`);

            if (coinCount % 10 === 0) {
                console.log(`Congratulations! You have collected ${coinCount} Torcoins.`);
            }
        } else {
            console.log("Not enough energy to collect Torcoin!");
        }
    }

    function rechargeEnergy() {
        let lastUpdated = parseInt(localStorage.getItem(lastUpdatedKey)) || Date.now();
        let now = Date.now();
        let elapsedSeconds = Math.floor((now - lastUpdated) / 1000);

        if (elapsedSeconds > 0 && energyCount < maxEnergy) {
            let newEnergyCount = Math.min(maxEnergy, energyCount + elapsedSeconds * rechargeSteps);
            let rechargeAmount = newEnergyCount - energyCount;
            energyCount = newEnergyCount;
            localStorage.setItem('energyCount', energyCount.toString());
            localStorage.setItem(lastUpdatedKey, now.toString());
            updateEnergyCount();
            if (rechargeAmount > 0) {
                console.log(`Energy recharged by ${rechargeAmount}. Current energy: ${energyCount}`);
            }
        }
    }

    document.getElementById('collect-button').addEventListener('click', collectTorCoin);

    updateCoinCount();
    updateEnergyCount();
    rechargeEnergy();

    setInterval(rechargeEnergy, 1000);

    function switchSection(event) {
        const switcher = event.currentTarget.getAttribute('data-switcher');
        document.querySelectorAll('.section').forEach(section => {
            section.classList.remove('active');
        });
        document.getElementById(`section-${switcher}`).classList.add('active');
    }

    document.querySelectorAll('.footer_box').forEach(footer_box => {
        footer_box.addEventListener('click', switchSection);
    });
}

